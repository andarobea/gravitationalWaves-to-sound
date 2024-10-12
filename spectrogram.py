import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.signal import get_window
from scipy.fftpack import fft

def spectrogram(signal, fs, window_size):
    n = len(signal)
    num_of_windows = n // window_size

    # Frequency and time arrays
    f = np.linspace(0, fs / 2, window_size)
    t = np.arange(num_of_windows) * (window_size / fs)

    S = np.zeros((window_size, num_of_windows))  # Allocate space for the spectrogram
    H = get_window('hann', window_size)  # Hanning window

    for i in range(num_of_windows):
        startW = i * window_size  # Start index of the window
        finalW = startW + window_size  # End index of the window
        windowedSignal = signal[startW:finalW] * H  # Apply Hanning window
        Y = fft(windowedSignal, 2 * window_size)  # FFT with zero-padding

        Y = Y[:window_size]  # Take only the positive frequencies
        S[:, i] = np.abs(Y)  # Store the magnitude in the spectrogram

    return S, f, t

def plot_spectrogram(S, f, t, window_title):
    plt.figure()
    plt.imshow(np.log10(S), aspect='auto', origin='lower', extent=[t.min(), t.max(), f.min(), f.max()], cmap='jet')
    plt.colorbar(format='%+2.0f dB')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title(window_title)
    plt.savefig('spectrogram.png')
    plt.close()

# Read the .wav file
fs, sig = wavfile.read('gravitational_wave_sound.wav')

# If the signal is stereo, convert to mono
if sig.ndim > 1:
    sig = sig.mean(axis=1)

# Normalize the signal
sig = sig / np.max(np.abs(sig))

window_size = 512
S, f, t = spectrogram(sig, fs, window_size)
plot_spectrogram(S, f, t, "Gravitational Wave Spectrogram")

