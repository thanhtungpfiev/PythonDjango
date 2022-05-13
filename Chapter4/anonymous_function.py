# Created by tung.dao thanhtungpfiev@gmail.com at 5/13/2022
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))


res = get_multiples_of_five(100)

adder_lambda = lambda a, b: a + b

res1 = adder_lambda(1, 2)

to_upper_lambda = lambda s: s.upper()

res2 = to_upper_lambda('abc')
