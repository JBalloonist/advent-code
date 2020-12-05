
def find_twenty(numbers, sum_result=2020):
    """
    Finds two numbers from a list that sum to sum_result and returns them

    >>> find_twenty([2005, 10, 0, 8, 7])
    (2005, 8, 7)
    """
    for n, first in enumerate(numbers):
        for j, second in enumerate(numbers):
            for i, third in enumerate(numbers):
                if n == j and j == i:
                    continue
                total = first + second + third
                if total == sum_result:
                    return first, second, third

def main():
    with open('numbers.txt', 'r') as out:
        numbers = out.read()
        numbers = [int(i) for i in numbers.split()]

    result = find_twenty(numbers)
    prod = lambda x, y, z : x * y * z
    print(prod(result[0], result[1], result[2]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
