import numpy as np

def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    medians = []
    for i in range(len(values) + 1):
        if i < window_size:
            continue 
        medians.append(np.median(values[i - window_size:i]))

    return medians
        