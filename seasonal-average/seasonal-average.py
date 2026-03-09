import numpy as np

def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    average = []
    for i in range(period):
        values = series[i::period]
        average.append(float(np.mean(values)))
    return average