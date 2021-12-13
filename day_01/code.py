import io


def clean_data(file):
    data = []
    with io.open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            data.append(int(line))
    return data


def count_intervals(data):
    count = 0
    for i in range(len(data) - 1):
        curr = data[i]
        next = data[i + 1]
        if curr < next:
            count += 1
    return count


def count_sliding_window_intervals(data):
    count = 0
    for i in range(len(data) - 3):
        curr = data[i]
        next = data[i + 3]
        if curr < next:
            count += 1
    return count


data = clean_data('data.txt')
print(count_intervals(data))
print(count_sliding_window_intervals(data))
