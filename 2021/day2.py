import argparse
from typing import DefaultDict

def get_data(file):
    """
    docstring
    """
    with open(file) as target:
        return target.readlines()


def split_input(lines):
    """
    >>> split_input(['forward 5', 'down 5'])
    [['forward', '5'], ['down', '5']]
    """
    return [line.split() for line in lines]

# need to differentiate between forward and up and down
def get_totals(split_input):
    """
    docstring
    """    
    all_dict = DefaultDict(list)
    for k, v in split_input:
        all_dict[k].append(int(v))
    
    return {k: sum(v) for k, v in all_dict.items()}

def get_multiplier(totals):
    return totals['forward'] * (totals['up'] - totals['down'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    opts = parser.parse_args()
    data = get_data(opts.file)
    input = split_input(data)
    totals = get_totals(input)
    print(get_multiplier(totals))
