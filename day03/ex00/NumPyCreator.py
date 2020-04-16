#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 12:52:12 by darodrig          #+#    #+#              #
#    Updated: 2020/04/16 12:52:14 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def from_list(lst, type=None):
    return np.array(lst, type)


def from_tuple(tpl, type=None):
    return np.array(tpl, type)


def from_iterable(itr, type=None):
    return np.array([elem for elem in itr], type)


def from_shape(shape, value, type=None):
    return np.full(shape, value, type)


if __name__ == "__main__":
    print(from_list([1, 2, 3.9, 4, 5], int),)
    print(from_tuple((1, 2, 3, 4, 5), float))
    print(from_iterable(map(lambda x: x * 2, range(4))))
    print(from_iterable("abcdefg"))
    print(from_shape((5, 5), 1.99, int))
