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
        elif previous == measurement:
            return 'no change'
        else:
            return 'decreased'


def get_count(measure_dict):
    """
    docstring
    """
    return Counter(measure_dict.values())


def create_groups(measurements):
    """
    docstring
    """
    return {f'Group_{n}':measurements[n: n+3] for n, vals in enumerate(measurements) if len(measurements[n: n+3]) == 3}


def group_sums(group_dict):
    """
    docstring
    """
    return {key: sum(value) for key, value in group_dict.items()}


if __name__ == "__main__":
    with open('test.txt', 'r') as out:
        data = [int(i) for i in out.readlines()]

    increases = {f'{n}-{val}': increase_decrease(val, data, n) for n, val in enumerate(data)}

    print(get_count(increases))

    group_dict = create_groups(data)

    group_sums_dict = group_sums(group_dict)

    print(group_sums_dict)

    group_data = list(group_sums_dict.values())
    print(f'group data: {group_data}')

    group_increases = {f'{n}-{val}': increase_decrease(val, group_data, n) for n, val in enumerate(group_data)}

    print(group_increases)

    print(get_count(group_increases))