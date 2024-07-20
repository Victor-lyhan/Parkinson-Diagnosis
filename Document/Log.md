# Software Log
**This file is used for documenting and development of the system.**
## July 20th 2024
### Computer Vision
* Normal Data vs patient data graphing
```
    Patient Data Statistics:
    count    3255.000000
    mean        0.033415
    std        97.032716
    min     -1794.957389
    25%       -33.511011
    50%         0.627522
    75%        31.732623
    max      1320.504493
    Name: linear_acceleration, dtype: float64
    Normal Data Statistics:
    count    7311.000000
    mean        0.057500
    std        71.020173
    min      -729.699033
    25%       -27.280563
    50%         0.496289
    75%        28.309368
    max       677.486215
    Name: linear_acceleration, dtype: float64
```
* Comparing std, min and max might be able to tell parkinson's

Note:
* live Assessment - doable
* CV methods: research needed
    * Hand tremor detection - datasets, reach out to hospitals(standards)
    * Turning in place
    * Walking 
* ideas for more data that can extracted from the video __(Research needed)__:
    - Turning Duration - difficult to set the standard
    - Turning smoothness
        - angular velovity and acceleration
    - Number and __length__ of Steps per Turn
        - Parkinson's patients often take smaller, shuffling steps, resulting in a higher step count for the same turn
        - Reduced step length and stride length are common in Parkinson's patients.
    - Postural Stability and Sway:
        - Assess the stability and balance during the turn.
    - __Initiation and Termination of Turns__:
        - Parkinson's patients may have difficulty starting or stopping movements (bradykinesia).
    * __different models?Training?__


## July 19th 2024
### Computer Vision  
* Video frame analysis ran on normal person * 2 -- NP1_1, NP1_2
    * Two video data compared with each other to validate discrepency 
        - Two graphs basically overlaped, meaning that the characteristics of data are consistent
    * Normal data compared with patient data trying to identify the possible marker
        - Can't tell any obvious difference using basic graphing 
        - found some algorithms that look for differences in dataframe
            - tested two, finish the rest tomorrow 
* ideas for more data that can extracted from the video:
    - Turning Duration
    - Turning smoothness
        - angular velovity and acceleration
    - Number and length of Steps per Turn
        - Parkinson's patients often take smaller, shuffling steps, resulting in a higher step count for the same turn
        - Reduced step length and stride length are common in Parkinson's patients.
    - Postural Stability and Sway:
        - Assess the stability and balance during the turn.
    - Initiation and Termination of Turns:
        - Parkinson's patients may have difficulty starting or stopping movements (bradykinesia).
    * __different models?Training?__