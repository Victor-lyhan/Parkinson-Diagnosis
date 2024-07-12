import math
import time
# from glob import global
from pathlib import Path
import glob
import cv2
import pandas as pd
from pydantic import BaseModel
from ultralytics import YOLO

# We want to be able to resize images by scale factor. It is acommon practice to preprocess images in computer vision models
scale_factor = 0.5
def resize_image(image, scale_factor):
    # Calculate the new dimensions
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    return resized_image

# Defines constants corresponding to different parts of the body
class GetKeypoint(BaseModel):
    NOSE: int = 0
    LEFT_EYE: int = 1
    RIGHT_EYE: int = 2
    LEFT_EAR: int = 3
    RIGHT_EAR: int = 4
    LEFT_SHOULDER: int = 5
    RIGHT_SHOULDER: int = 6
    LEFT_ELBOW: int = 7
    RIGHT_ELBOW: int = 8
    LEFT_WRIST: int = 9
    RIGHT_WRIST : int =10 
    LEFT_HIP: int = 11
    RIGHT_HIP: int = 12
    LEFT_KNEE: int = 13
    RIGHT_KNEE: int = 14
    LEFT_ANKLE: int = 15
    RIGHT_ANKLE: int = 16

get_keypoint = GetKeypoint()

for source_path in glob('Parkinsons-Project/data/video-sensor-data/PDFE01_1.csv'):
    name = Path(source_path).stem

    # Open video capture
    cap = cv2.VideoCapture(source_path)
    model = YOLO('yolov8n-pose.pt')

    # Create variables for angles, angular velocity and linear acceleration to calcualte the movemement
    prev_angle = None
    prev_angular_velocity = None
    prev_linear_velocity = None
    linear_acceleration = None
    angulat_velocity = None

    # Need to know the time as well to measure the above
    prev_time = 0
    data_list = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        try:
            # Resize the image & get current frame time
            frame = resize_image(frame, scale_factor)
            current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

            # Get the results from the yolo model at that current frame with a 0.7 conf
            results = model(frame, conf = 0.7)
            index = 0
            
            # Retrieve keypoints from the result and takes their xyn coordinates
            # And converts it into a numpy array
            result_keypoint = results[0].keypoints.xyn.cpu().numpy

            # If there are more than one set of keypoints detected
            # Compare the x-coordinate of RIGHT_ANKLE between [0] and [1] 
            # Assuming the higher x-coordinate is the right ankle
            # Which one is more likely to represent the right ankle?
            if len(result_keypoint) > 1 and result_keypoint[0][get_keypoint.RIGHT_ANKLE][0] > result_keypoint[1][get_keypoint.RIGHT_ANKLE][0]:
                index = 1
            print('index', index)

            # Extract the keypoints
            right_ankle = result_keypoint[index][get_keypoint.RIGHT_ANKLE]
            right_knee = result_keypoint[index][get_keypoint.RIGHT_KNEE]
            right_hip = result_keypoint[index][get_keypoint.RIGHT_HIP]

            # Calculate the vectors
            vector1 = (right_knee[0] - right_ankle[0], right_knee[1] - right_ankle[1])
            vector2 = (right_hip[0] - right_ankle[0], right_hip[1] - right_ankle[1])

            # Caclualte the angle between vectors
            dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
            magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
            magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)
            angle_rad = math.acos(dot_product/(magnitude1*magnitude2))

            # Convert to degrees
            angle_deg = math.degrees(angle_rad)

            # Get the time difference
            time_diff = current_time - prev_time

            # Calculate the angular velocity
            if prev_angle is not None:
                angular_velocity = (angle_deg - prev_angle) / time_diff
                print(f'Angular Velocity: {angular_velocity} deg/s')

            # Calculate linear acceleration
            if prev_angular_velocity is not None:
                linear_acceleration = (angular_velocity - prev_angular_velocity)
            
            # Update variables
            prev_angle = angle_deg
            prev_angular_velocity = angular_velocity
            prev_linear_acceleration = linear_acceleration
            prev_time = current_time

            data_list.append({'time': current_time, 'linear_acceleration': linear_acceleration, 'angular_velocity': angular_velocity})
        except Exception as e:
            print(e)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    df = pd.DataFrame(data_list)
    df.to_csv(f'dataset/{name}.csv')