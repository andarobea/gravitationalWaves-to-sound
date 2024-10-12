## Transforming the data from the LISA mission into human audible sounds

    Summary:

    -create an array containing the LISA data(I used less data for testing purposes)
    -get the magnitude of the wave using the X Y Z coordinates and normalize the array
    -rescale time to the desired length for the audio file
    -interpolate the magnitude to fit the rescaled time
    -use a low-pass filter to change the frequency of the signal so that the frequency is between 2000-20000 Hz
    -downshift is necessary
    -make .wav file
    -plot the results
    -create spectrogram of the .wav file for better visualisation
