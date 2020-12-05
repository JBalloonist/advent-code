import functools
import operator
import sys


def get_nums_that_sum_to(seq, sum_result=2020):
    """
    This function takes a sequence of numbers
    finds two that sum to sum_result and returns them

    >>> get_nums_that_sum_to([2020,10,0])
    (2020, 0)

    """
    for i, val in enumerate(seq):
        for j, val2 in enumerate(seq):
            if i == j:
                continue
            if val + val2 == sum_result:
                return val, val2

def get_nums_that_sum_to_part2(seq, sum_result=2020):
    """
    This function takes a sequence of numbers
    finds two that sum to sum_result and returns them

    >>> get_nums_that_sum_to_part2([2010,10,0])
    (2010, 10, 0)

    """
    for i, val in enumerate(seq):
        for j, val2 in enumerate(seq):
            for k, val3 in enumerate(seq):
                if i == j == k:
                    continue
                if val + val2 + val3 == sum_result:
                    return val, val2, val3
    
def main(args):
    fname = args[-1]
    res = get_nums_that_sum_to_part2([int(line.strip()) for line in open(fname)])
    #import pdb;pdb.set_trace()
    print(functools.reduce(operator.mul, res))

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    main(sys.argv)



