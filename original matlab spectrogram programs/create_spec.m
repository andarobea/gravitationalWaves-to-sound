clear;

window_size = 512;
low_pass_cutoff = 1000; % Hz

[sig, fs] = audioread("gravitational_wave_sound.wav");
% sig = stereo_to_mono(sig);

mono = mean(sig,2);  % stereo to mono
mono = mono / max(abs(mono));

[S f t] = spectrogram(mono, fs, window_size);

plot_spectrogram(S, f, t, "gravitational wave spectrogram");