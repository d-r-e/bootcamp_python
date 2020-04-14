from operator import add, mul
from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    res = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for each in list_of_inputs[2:]:
        res = function_to_apply(res, each)
    return res


if __name__ == '__main__':
    print("ft_reduce:   " + str(ft_reduce(add, range(7))))
    print("reduce   :   " + str(reduce(add, range(7))))
    print("ft_reduce:   " + str(ft_reduce(mul, range(1, 10))))
    print("reduce   :   " + str(reduce(mul, range(1, 10))))
