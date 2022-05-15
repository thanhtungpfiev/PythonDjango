# Created by Admin at 5/15/2022
def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))


for n in print_squares(2, 5):
    print(n)
