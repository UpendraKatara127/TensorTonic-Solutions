import  numpy as np
def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    series = np.array(series)
    mean = np.mean(series)
    variance = np.var(series)
    autoCor = []

    if variance == 0:
        return [1.0] + [0.0] * max_lag
    for k in range(max_lag + 1):
        if k == 0:
            autoCor.append(1.0)
        else:
            numerator = np.sum((series[k:] - mean) * (series[:-k] - mean))
            denominator = len(series) * variance
            autoCor.append(numerator/denominator)
    return autoCor