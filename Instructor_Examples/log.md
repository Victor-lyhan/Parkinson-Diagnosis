# Log

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