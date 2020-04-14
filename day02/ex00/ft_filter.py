#! /usr/bin/env python3


def ft_filter(function_to_apply, list_of_inputs):
    return [each for each in list_of_inputs if function_to_apply(each)]


if __name__ == '__main__':
    chars = "aBcDeFg"
    symb = "abcd-x??ds3f"
    print(list(ft_filter(str.isupper, chars)))
    print(list(filter(str.isupper, chars)))
    print(list(ft_filter(str.isalnum, symb)))
    print(list(filter(str.isalnum, symb)))
