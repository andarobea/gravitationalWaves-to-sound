import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

# Open the WAV file
spf = wave.open("gravitational_wave_sound.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.frombuffer(signal, dtype=np.int16)

# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

plt.figure(figsize=(10, 4))
plt.title("Signal Waveform")
plt.plot(signal)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)

# Save the plot as PNG
plt.savefig('gravitational_wave_sound_plot.png')

# Optionally, show the plot interactively (if supported)
# plt.ion()  # Uncomment this line to force interactive mode
# plt.show()
