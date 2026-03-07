def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    change = []
    for i in range(1, len(series)):
        if series[i-1] ==  0:
            change.append(0.0)
        else:
            numerator = series[i] - series[i-1]
            change.append(numerator / series[i-1])
    return change