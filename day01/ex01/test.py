#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 12:36:21 by darodrig          #+#    #+#              #
#    Updated: 2020/04/13 12:36:21 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from game import GotCharacter, Stark

if __name__ == "__main__":
	arya = Stark("Arya")
	print(arya.__dict__)
	arya.print_house_words()
	print(arya.is_alive)
	arya.die()
	print(arya.is_alive)