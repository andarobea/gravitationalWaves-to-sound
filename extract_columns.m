function [time X Y Z] = extract_columns()
    % M = dlmread('/mnt/c/Users/sorin/OneDrive/Desktop/intern_iss/LDC1-1_MBHB_v1_1_FD_noiseless.txt', ' ', 1, 0);
    M = dlmread('/mnt/c/Users/sorin/OneDrive/Desktop/intern_iss/test.txt', ' ', 1, 0);
    time = M(:, 1);
    X = M(:, 2);
    Y = M(:, 3);
    Z = M(:, 4);
    save('gravitational_wave_data.mat', 'time', 'X', 'Y', 'Z', '-v7');
    % -v7 needed for the python3 import
    % for human readable contents use save('gravitational_wave_data.mat', 'time', 'X', 'Y', 'Z');
endfunction
