with open('test_data.txt', 'r') as out:
    lines = out.readlines()

trees = []
line_start = 1
pos_start = 3
for l_num, line in enumerate(lines):
    for pos_num, location in enumerate(line):
        if pos_num == pos_start and l_num == line_start:
            trees.append(location)
            print(f'line: {l_num}  position: {pos_num}')
            line_start += 1
            pos_start += 3

print(trees)