from sys import argv
from collections import Counter

def main(lines):
    """
    docstring
    """
    trees = []
    line_start = 1
    pos_start = 3
    for l_num, line in enumerate(lines):
        for pos_num, location in enumerate(line):
            if pos_num == pos_start and l_num == line_start:
                print(f'Line Number: {l_num}; Line: {line};\
                Loc: {location}; Pos_num: {pos_start}')
                trees.append(location)
                line_start += 1
                pos_start += 3
            if (len(line) // 3) % 10 == 0:
                pos_start = 3

    return Counter(trees)


if __name__ == "__main__":
    fname = argv[1]
    with open(fname, 'r') as out:
        lines = out.readlines()
    
    print(main(lines))
