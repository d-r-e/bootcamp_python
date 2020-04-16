#! /usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    NumPyCreator.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: darodrig <darodrig@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 12:52:12 by darodrig         #+#    #+#              #
#    Updated: 2020/04/16 13:11:01 by darodrig        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import numpy as np


class NumPyCreator:

    @staticmethod
    def from_list(lst, type=None):
        return np.array(lst, type)

    @staticmethod
    def from_tuple(tpl, type=None):
        return np.array(tpl, type)

    @staticmethod
    def from_iterable(itr, type=None):
        return np.array([elem for elem in itr], type)

    @staticmethod
    def from_shape(shape, value, type=None):
        return np.full(shape, value, type)


if __name__ == "__main__":
    npc as NumPyCreator

    print(npc.from_list([1, 2, 3.9, 4, 5], int))
    print(npc.from_tuple((1, 2, 3, 4, 5), float))
    print(npc.from_iterable(map(lambda x: x * 2, range(4))))
    print(npc.from_iterable("abcdefg"))
    print(npc.from_shape((5, 5), 1.99, int))
