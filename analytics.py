
def calculatemean(data):
    """Return the average of a list of numbers."""
    if not data:
        print("Error: Cannot calculate mean of empty list.")
        return None
    return sum(data) / len(data)


def calculatemedian(data):
    """Return the middle value of a sorted list."""
    if not data:
        print("Error: Cannot calculate median of empty list.")
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_data[mid])
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2


def calculatemode(data):
    """Return the value that appears most often."""
    if not data:
        print("Error: Cannot calculate mode of empty list.")
        return None
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    return max(frequency, key=frequency.get)


def calculatevariance(data):
    """Return the average of squared differences from the mean."""
    if not data:
        print("Error: Cannot calculate variance of empty list.")
        return None
    mean = calculatemean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def calculatestddeviation(data):
    """Return the square root of the variance."""
    if not data:
        print("Error: Cannot calculate std deviation of empty list.")
        return None
    return calculatevariance(data) ** 0.5


def calculatecorrelation(x, y):
    """Return Pearson correlation coefficient between two lists."""
    if not x or not y:
        print("Error: Cannot calculate correlation of empty lists.")
        return None
    if len(x) != len(y):
        print("Error: Lists must be the same length for correlation.")
        return None

    n = len(x)
    mean_x = calculatemean(x)
    mean_y = calculatemean(y)

    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    std_x = calculatestddeviation(x)
    std_y = calculatestddeviation(y)

    if std_x == 0 or std_y == 0:
        print("Error: Standard deviation is zero, correlation undefined.")
        return None

    return covariance / (std_x * std_y)


def calculatemovingaverage(data, windowsize):
    """Return list of averages using a sliding window."""
    if not data:
        print("Error: Cannot calculate moving average of empty list.")
        return None
    if windowsize <= 0 or windowsize > len(data):
        print("Error: Invalid window size.")
        return None

    result = []
    for i in range(len(data) - windowsize + 1):
        window = data[i : i + windowsize]
        result.append(sum(window) / windowsize)
    return result



def getsalestotals(transactions):
    """Extract total sale amounts from transactions list."""
    return [t["totalamount"] for t in transactions]


def getquantitiessold(transactions):
    """Extract quantities sold from transactions list."""
    return [t["quantitysold"] for t in transactions]
