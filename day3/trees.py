
def get_lines(file_input):
    """
    docstring
    """
    for line_num, line in enumerate(file_input):
        yield line_num, line


def get_location(line_input):
    """
    docstring
    """
    for pos, location in enumerate(line_input):
        yield(pos, location)

# move right three spaces
# down one line
# right three spaces again
def check_location(parameter_list):
    """
    docstring
    """
    pass


def main():
    with open('test_data.txt') as target:
        lines = get_lines(target.readlines())

    print(next(get_location(next(lines)[1])))


if __name__ == "__main__":
    main()
