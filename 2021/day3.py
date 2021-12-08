import argparse
from collections import Counter, defaultdict

def get_data(file):
    """
    docstring
    """
    with open(file) as target:
        return [v.strip('\n') for v in target.readlines()]


def split_nums(data):
    """
    docstring
    """
    d = defaultdict(list)
    for row in data:
        for loc,num in enumerate(row):
            d[loc].append(num)
    
    return d

def count_nums(split_nums):
    """
    docstring
    """
    # c = Counter()
    cnts = {k: {num: cnt for num, cnt 
        in sorted(dict(Counter(v)).items(), key=lambda item: item[1])} 
        for k, v in split_nums.items()}

    least = ''.join([list(val.keys())[0] for val in cnts.values()])
    most = ''.join([list(val.keys())[1] for val in cnts.values()])
    
    return least, most
    


def get_power(binary_nums):
    """
    docstring
    """
    return int(binary_nums[0], 2) * int(binary_nums[1], 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    opts = parser.parse_args()
    data = get_data(opts.file)
    nums = split_nums(data)
    cnts = count_nums(nums)
    print (cnts)
    print(get_power(cnts))
