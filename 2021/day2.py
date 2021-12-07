import argparse

def get_data(file):
    """
    docstring
    """
    with open(file) as target:
        return target.read()


def parse_direction(dir):
    """
    >>> parse_direction('up')
    '-'
    >>> parse_direction('down')
    '+'
    """
    dir_dict = {'forward': '+', 'down': '+', 'up': '-'}
    return dir_dict[dir]


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
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    opts = parser.parse_args()
    data = get_data(opts.file)
    get_totals()