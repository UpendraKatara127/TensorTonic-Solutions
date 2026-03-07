def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    def ema(i):
        if i  == 0:
            return values[i]
        return (alpha * values[i]) + (1-alpha) * ema(i-1)
    expAvg = []
    for i in range(len(values)):
        expAvg.append(ema(i))
    return expAvg