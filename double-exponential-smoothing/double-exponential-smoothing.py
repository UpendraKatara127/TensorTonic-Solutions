def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here
    def des(i):
        if i == 0:
            return series[0], series[1] - series[0]
        l_prev, b_prev = des(i-1)
        l_t = alpha * series[i] + (1-alpha)*(l_prev + b_prev)
        b_t = beta*(l_t - l_prev) + (1-beta)*b_prev
        return l_t, b_t
    levels  = []
    for i in range(len(series)):
        l_t , _ = des(i)
        levels.append(l_t)
    return levels
        