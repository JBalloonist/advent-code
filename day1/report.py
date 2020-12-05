
def find_twenty(numbers, sum_result=2020):
    """
    Finds two numbers from a list that sum to sum_result and returns them

    >>> find_twenty([2020, 10, 0])
    (2020, 0)
    """
    for n, first in enumerate(numbers):
        for j, second in enumerate(numbers):
            if n == j:
                continue
            total = first + second
            if total == sum_result:
                return first, second

def main():
    with open('numbers.txt', 'r') as out:
        numbers = out.read()
        numbers = [int(i) for i in numbers.split()]

    result = find_twenty(numbers)
    prod = lambda x, y : x * y
    print(prod(result[0], result[1]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
