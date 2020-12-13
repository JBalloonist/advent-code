from sys import argv
from collections import Counter

def main(lines):
    """
    docstring
    """
    trees = []
    x_pos = 0
    for y_pos, line in enumerate(lines):
        line = line.strip()
        try:
            location = line[x_pos]
        except:
            line *= y_pos
            location = line[x_pos]

        count = Counter(trees)['#']
        
        print(f'x_pos: {x_pos} y_pos: {y_pos} count: {count} ')
        trees.append(location)
        x_pos += 3
    
    return Counter(trees)


if __name__ == "__main__":
    fname = argv[1]
    with open(fname, 'r') as out:
        lines = out.readlines()
    
    print(main(lines))
