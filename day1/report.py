

with open('numbers.txt', 'r') as out:
    numbers = out.read()

def find_twenty(numbers, sum_result=2020):
    for n, first in enumerate(numbers):
        for j, second in enumerate(numbers):
            if n == j:
                continue
            total = first + second
            if total == sum_result:
                print(total)
                print(f'first: {first} second: {second}')
                return first, second
                
find_twenty(numbers)
