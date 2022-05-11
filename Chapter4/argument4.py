# Created by tung.dao thanhtungpfiev@gmail.com at 5/11/2022
x = [1, 2, 3]


def func(x):
    x[1] = 42
    x = 'something else'


func(x)
print(x)
