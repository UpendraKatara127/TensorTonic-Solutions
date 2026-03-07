import numpy as np

def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    series = np.array(series)
    max_lag = max(lags)
    X = []
    for i in range(max_lag, len(series)):
        row = []
        for lag in lags:
            row.append(series[i - lag])
        X.append(row)
    return X
    