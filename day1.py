from collections import Counter

def increase_decrease(measurement, measure_list, loc):
    """
    docstring
    """
    loc = loc - 1
    previous = measure_list[loc]
    # print(f'loc: {loc}')
    # print(f'Previous value: {previous}  Current value: {measurement}')

    if loc < 0:
        return 'N/A'
    else:
        if previous < measurement:
            return 'increased'
        else:
            return 'decreased'


def get_count(measure_dict):
    """
    docstring
    """
    return Counter(measure_dict.values())


if __name__ == "__main__":
    with open('report.txt', 'r') as out:
        data = [int(i) for i in out.readlines()]

    increases = {f'{n}-{val}': increase_decrease(val, data, n) for n, val in enumerate(data)}

    # print(increases[:10])
    print(get_count(increases))