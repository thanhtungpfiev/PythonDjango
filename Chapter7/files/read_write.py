# Created by Admin at 5/18/2022
with open('fear.txt') as f:
    lines = [line.rstrip() for line in f]

with open('fear_copy.txt', 'w') as fw:
    fw.write('\n'.join(lines))

with open('fear_copy.txt') as fh:
    for line in fh:
        print(line.strip())
