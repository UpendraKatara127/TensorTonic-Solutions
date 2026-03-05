import numpy as np
def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    values = np.array(values, dtype=float)
    x = np.sort(values)
    length = len(values)
    if length < 2:
        return [0]
    median = np.median(values)
    lower = x[ : length//2]
    upper = x[(length + 1 )//2 : ]

    quartile_one = np.median(lower)
    quartile_third = np.median(upper)
    
    IQR = quartile_third - quartile_one
    if IQR == 0:
        return np.zeros_like(values)
    return (values - median) / IQR