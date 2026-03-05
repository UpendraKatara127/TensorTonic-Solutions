def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    max_val = max(values)
    min_val = min(values)
    if max_val == min_val:
        return [0] * len(values)
    bin_width = (max(values) - min(values)) / num_bins
    bins = []
    for val in values:
        bin_index = int((val - min_val) / bin_width)
        if bin_index == num_bins:
            bin_index -= 1
        bins.append(bin_index)
    return bins
        
    