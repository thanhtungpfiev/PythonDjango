# Created by Admin at 5/9/2022
def outer():
    test = 1
    def inner():
        nonlocal test
        test = 2
        print('inner:', test)
    inner()
    print('outer:', test)
test = 0
outer()
print('global:', test)
