def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]
    
def mean(data):
    return sum(data) / len(data)

def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

def standard_deviation(data):
    return variance(data) ** 0.5

def mode(data):
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = max(frequency.values())
    modes = [key for key, count in frequency.items() if count == max_count]
    return modes

def covariance(data1, data2):
    if len(data1) != len(data2):
        raise ValueError("Datasets must be of the same length")
    mean1 = mean(data1)
    mean2 = mean(data2)
    cov = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / len(data1)
    return cov

def correlation(data1, data2):
    cov = covariance(data1, data2)
    stddev1 = standard_deviation(data1)
    stddev2 = standard_deviation(data2)
    return cov / (stddev1 * stddev2)

def harmonic_mean(data):
    n = len(data)
    return n / sum(1 / x for x in data)

print("This is stats.py in mathsinpython package")
print("Mean of [1, 2, 3, 4, 5]:", mean([1, 2, 3, 4, 5]))
print("Median of [1, 2, 3, 4, 5]:", median([1, 2, 3, 4, 5]))
print("Variance of [1, 2, 3, 4, 5]: ", variance([1, 2, 3, 4, 5]))
print("Standard Deviation of [1, 2, 3, 4, 5]:", standard_deviation([1, 2, 3, 4, 5]))
print("Mode of [1, 2, 2, 3, 4]:", mode([1, 2, 2, 3, 4]))
print("Covariance of [1, 2, 3] and [4, 5, 6]:", covariance([1, 2, 3], [4, 5, 6]))
print("Correlation of [1, 2, 3] and [4, 5, 6]:", correlation([1, 2, 3], [4, 5, 6]))
print("Harmonic Mean of [1, 2, 3, 4, 5]:", harmonic_mean([1, 2, 3, 4, 5]))  