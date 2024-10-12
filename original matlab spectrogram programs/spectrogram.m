function [S, f, t] = spectrogram(signal, fs, window_size)
    n = length(signal);
    num_of_windows = floor(n / window_size);

    f = zeros(window_size, 1);
    f = (0:window_size - 1) * (fs/2) / window_size; % frecventa nyquist: fs/2
    f = f'; % coloana

    t = zeros(num_of_windows, 1);
    t = (0 : num_of_windows - 1) * (window_size / fs);  % formula
    t = t'; % coloana

    S = zeros(window_size, num_of_windows); % Aloca S
    H = hanning(window_size);
    for i = 1 : num_of_windows
        startW = (i - 1) * window_size + 1; % indice de inceput
        finalW = startW + window_size - 1;  % indice de final
        windowedSignal = signal(startW : finalW) .* H;  % aplicare hanning
        Y = fft(windowedSignal, 2 * window_size); % fast fourier transform

        Y = Y(1 : window_size);  % doar partea reala

        S(:, i) = abs(Y); % pun in spectrograma
    end
end

