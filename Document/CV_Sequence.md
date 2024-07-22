# Video Analysis Running Sequence
## 1. Video-Sensor-Analysis
* Breaks the video down to frames
* Does calculation on each frame: frame_time, angular velocity, angular acceleration
* Stores data in a df
* Puts the df in a folder

## 2.Vid-Stats-Concatenation
* Adds all videos(in the folder) linear acceleration stats (average: __stdv__, min, max, mean, ...) to a df

##