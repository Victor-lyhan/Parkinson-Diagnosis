# Software Log
**This file is used for documenting and development of the system.**
## July 27th 2024
### Computer Vision
* Code organized
* Models in folder
* still need to tune the model
    * checking the accuracy over all files

## July 26th 2024
### Computer Vision
* Tried training the model using 1 parameter vs multiple
* Tried predicting differnt parameter
    * Which one has the best accuracy

* p1v1 
    * Given std input: 83.57921565783211 
    * Prediction: 

| Parameter | Predicted | Original | MSE |
|---|---|---|---|
| FoG Ratio | 22.428913 | 95.9 | 1322 |
| UPDRS-II | 6.8395505 | 6 | 7.247766800645755 |
| UPDRS-III | 25.10884 | 16 | 142.3441821694842 |
| PIGD | 5.191346 | 6 | 9.992495622697167 |
| Dyskinesia* | 0.7922452 | 0 | 8.662053932808194 | 
| MiniBestTest Score | 21.518253 | 17 | 26.389296815497314 |
| TUG time | 12.618898 | 16.73 | 25.621056229161052 |
| TUG dual-task time | 17.992321 | 28.43 | 221.43037963658153 |

* Decided to use NN as it has the lowest error meaning the highest accuracy
    * 5 layers
    * still need to tune the model


## July 25th 2024
### Computer Vision
* Continue on using ml algorithms to determine correlations between std with all other parameters
    * Used CNN 
* All progress commented in the graph.ipynb
* Whole process works:
    * Next step: tuning the parameters
    * Making the complete loop/code
    
## July 23rd 2024
### Computer Vision
* Problem 1
    * Outliers - getting rid of or no - matters or no
        * correlation between ang acc - fog ratio - doesn;t correlate
            * Results: Using heatmap, no significant difference between three values shown before and after large values were deleted - no linear model
            * Bigger dataset needed, higher dimensions
        * 
* Problem 2
    * Weighted avg 

### PDFEinfo.csv
* Parameters reflecting motor performace      
```
Session 1 - UPDRS-II (score): This assesses motor experiences of daily living.
Session 1 - UPDRS-III (score): This evaluates motor examination.
Session 1 - PIGD (score): Postural Instability and Gait Difficulty score.
Session 1 - Dyskinesia (score): Evaluates involuntary movements.
Session 1 - MiniBestTest (score): Assesses balance.
Session 1 - TUG time (s): Timed Up and Go test for mobility.
Session 1 - TUG dual-task time (s): Timed Up and Go test with a dual task for mobility and multitasking ability.
``` 


## July 22nd 2024
### Computer Vision
* Code for getting merging the fog ratio and updrs-3 score into stats - df
    * Can be used to compare fog Ratio to stats
* Logic:
    * We have angular acceleration data for all videos
    * Instead of taking the avg of all angular accel ->  Figure out the correlation between fog ratio and the angular accel
    * higher angular accel -> higher stdv, vice versa  
* graphed angualr accel vs fog ratio
    * seems to be no correlation for now: one of the possible reasons include having irregularl huge values in df that messes up the stats
    * meaning that figuring out a strategy to get rid of em is necessary
    
## July 21st 2024
### Computer Vision
* Video Sensor Analysis: Data acquested from all videos - in All folder
    ```
    Results:
    all_stats : patient data - all stats
    all_stats_angularAcceleration: patient data - only angular acceleration stats
    np_all_stats: ...
    np_all_stats_angularAcceleration: ...

    ```
* Got the avg - min, max, avg, stdv for patient and non patient
    * noticed some reall big values -> getting rid of those without bias(intentionally selecting the acceptable range)
* correlation between stats for each video and the FoG Ratio and UPDRS-III
    * code for creating df with angular acceleration, fog ration, updrs - 3 used for comparison ml

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

TODO: 
1. Use the standard deviation to determine parkinsons or not (create a threshold)
    1. you want to find the average of all the patients(need to make sure that all the patients parkinsonns), compare that to data of patient withuot parkinsons, With that information, you can apply different ml models
2. Finding hand/finger tremor dataset

Video Sensor Analysis:
* Some df has large values that are impractical
* Need to relate the statistical data with the updrs score, forming the scale standard


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