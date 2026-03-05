
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    rows = len(data)
    cols = len(data[0])
    mins = [min(data[i][j] for i in range(rows)) for j in range(cols)]
    maxs = [max(data[i][j] for i in range(rows)) for j in range(cols)]
    result = [[0] * cols for rows in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if maxs[j] == mins[j]:
                result[i][j] = 0
            else:
                result[i][j] = (data[i][j] - mins[j]) / (maxs[j] - mins[j])
    return result
    