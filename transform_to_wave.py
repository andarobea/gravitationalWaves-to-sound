import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.io import loadmat
from scipy.signal import butter, filtfilt
from scipy.interpolate import interp1d
import numpy.fft as fft

# Load the .mat file
data = loadmat('gravitational_wave_data.mat')

# Extract variables
time = data['time'].flatten()
x = data['X'].flatten()
y = data['Y'].flatten()
z = data['Z'].flatten()

# Combine the data into a single signal (magnitude of the vector)
magnitude = np.sqrt(x**2 + y**2 + z**2)

# # plot original data
# plt.figure(figsize=(10, 4))
# plt.plot(time, magnitude)
# plt.title('Original Signal')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.savefig('original_data.png')
# plt.close()

# Rescale time to bring into the audible range
original_duration = time[-1] - time[0]
desired_duration = 5  # in seconds
sampling_rate = 44100

# Number of samples in the desired duration
number_of_samples = int(sampling_rate * desired_duration)

# Normalize the magnitude to the range [-1, 1]
normalized_magnitude = magnitude / np.max(np.abs(magnitude))

# Rescale the time vector to fit the desired duration
rescaled_time = np.linspace(0, original_duration, number_of_samples)

# plt.figure(figsize=(10, 4))
# plt.plot(time, normalized_magnitude)
# plt.title('Normalized Signal')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.savefig('normalized_data.png')
# plt.close()

# Interpolate the normalized data to fit the desired number of samples
interp_func = interp1d(time, normalized_magnitude, kind='cubic')
interpolated_signal = interp_func(rescaled_time)

print("Interpolated Signal:", interpolated_signal[:10])  # Print first 10 values for inspection

# Plot the interpolated signal
plt.figure(figsize=(10, 4))
plt.plot(rescaled_time, interpolated_signal)
plt.title('Interpolated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('interpolated_signal.png')
plt.close()

# Define a low-pass filter
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def apply_lowpass_filter(data, cutoff_freq, fs):
    b, a = butter_lowpass(cutoff_freq, fs)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Define cutoff frequency for the low-pass filter (in Hz)
low_pass_cutoff = 2000  # Adjust as needed based on your signal characteristics

# Apply low-pass filter to the interpolated signal
filtered_signal = apply_lowpass_filter(interpolated_signal, low_pass_cutoff, sampling_rate)
print("Filtered Signal:", filtered_signal[:10])  # Print first 10 values for inspection

# Plot the filtered signal
plt.figure(figsize=(10, 4))
plt.plot(rescaled_time, filtered_signal)
plt.title('Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('filtered_signal.png')
plt.close()

# Apply frequency downshifting (e.g., by a factor of 10) to convert to audible range
downshift_factor = 10
downshifted_time = np.linspace(0, desired_duration / downshift_factor, number_of_samples)
interp_func = interp1d(downshifted_time, filtered_signal, kind='cubic')
shifted_signal = interp_func(downshifted_time)

print("Shifted Signal:", shifted_signal[:10])  # Print first 10 values for inspection

# Plot the shifted signal
plt.figure(figsize=(10, 4))
plt.plot(rescaled_time, shifted_signal)
plt.title('Shifted Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('shifted_signal.png')
plt.close()

# Convert to 16-bit PCM format
audio_signal = np.int16(shifted_signal / np.max(np.abs(shifted_signal)) * 32767)

# Write the audio signal to a WAV file
write('gravitational_wave_sound.wav', sampling_rate, audio_signal)

