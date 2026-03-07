import numpy as np

def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    ma = []
    n = len(values)
    for i in range(window_size, len(values) + 1):
        sum = 0
        for j in range(i - window_size, i):
            sum += values[j]
        ma.append(sum / window_size)
    return ma
    