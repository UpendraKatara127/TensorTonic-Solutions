def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    for i in range(len(values)):
        if values[i] is None:
            prev = i - 1
            next = i + 1
            while values[next] is None:
                 next += 1
            values[i] = values[prev] + (values[next] - values[prev]) * ((i-prev)/(next-prev))
        else: continue 
    return values

    