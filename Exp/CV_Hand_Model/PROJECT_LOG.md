## November 19, 2024
* Started implementing the LSTM Model
    * We needed to create labels for pos and neg patients

Next class, we want to test the LSTM NN Model -> But that requires more data b/c there was an error with train test split
saying that splitting the data will create an empty sequence (b/c there is not enough data)

### Novemeber 11, 2024
* Create a way to determine parkinsons based on .csv data
    * In this case, we are using change in velocity
    * Also consider the landmark (joint on the hand) that can contribute to parkinsons
* We need to analyze the data that we have in order to determine what direction to go now
    * We need to compare results from positive and neg patients
        * compare velocity
        * compare acc
        * compare averages
        * compare graphs
    * Once we determine where the difference is... we can go from there
* If there is not enought data to do comparisons, we can determine which landmark is the most significant
    * If we know which landmark is the most significant, we can cut down future work for later by focusing on that
* LSTM
    * Use frequency analysis techniques, such as a Fast Fourier Transform (FFT), on the x, y, and z coordinates of each hand landmark across frames. Tremors typically have a characteristic frequency range (around 4-6 Hz for Parkinson’s tremors).


Next class, we will implement methodology of the research paper

[Link to Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8273850/)