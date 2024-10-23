# Log

## Oct 22, 2024
* We will calculate the acceleration
* We need to create a baseline so that we can determine the variance of parkinons vs baseline and non-parkinsons vs baseline
* We can create a script where it determines if the variance is higher at a certain point, then they probably have parkinosns/not


## October 8, 2024
* Did calculations of landmarks based on video data 
* Now we need to
    1. Gather video data of Parkinsons patient
    2. Figure out how to automize everything WHILE taking a video

## July 13, 2024
* Edited the code so that we can view the patietn videos using Ultralytics and Roboflow
* Updated the scirpt so that it records the results into a .csv file for further analysis

## July 16, 2024
* We can take a look at the PDFE_info.csv file and compare the active FOG times with the graphs created from the video data results. That means we will be comparing linear accelration (want to add angular acceleration) with the FOG ratio.

* Some time soon, we also want to go over every lien of code in the video analysis script

## July 26, 2024
* To train model using GPU, we need a few things
    - tensorflow-2.14.0
    - CUDA-12.3
    - cuDNN-8.9