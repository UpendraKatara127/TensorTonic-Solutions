import pandas as pd
def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here
    results = []
    for i in range(len(values)):
        if i < window_size - 1:
            continue 

        window = values[i - window_size  + 1 : i + 1]
        mean = sum(window) / window_size
        variance = sum((x - mean) ** 2 for x in window) / window_size
        results.append(math.sqrt(variance))
    return results
        
    