
def get_lines(file_input):
    """
    Generator that returns the each line of a text file.
    """
    for line in open(file_input, 'r'):
        yield line


def get_location(line_input):
    """
    docstring
    """
    for pos, location in enumerate(line_input):
        yield(pos, location)

# move right three spaces
# down one line
# right three spaces again
def track_location(line):
    """
    docstring
    """
    pass


def main():
    lines = get_lines('test_data.txt')
    # print(next(get_location(next(lines))))
    for string in lines:
        print(get_location(string))
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
