#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/09 16:46:11 by darodrig          #+#    #+#              #
#    Updated: 2020/04/09 16:46:11 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from time import sleep
import datetime
def ft_progress(lst):
	start = datetime.datetime.now()
	end = len(lst) * 0.005
	i = 0
	length = len(lst)
	for each in lst:
		i+=1
		time = datetime.datetime.now() - start
		
		s = time.microseconds/1000000 + time.seconds
		if each == lst[0]:
			eta = 0
			step = 0
		elif each == lst[1]:
			eta = s * len(lst)
			step = s
			eta = eta - step
		else:
			eta = eta -step
		percentage =int(i/len(lst) * 100)
		perc_count = int(percentage / 10)

		print('\r '+ "ETA: " + (str(round(eta - step, 2)) + "s").ljust(6, ' ')
			+ " [" + str(percentage).ljust(2) + "%]["
			+ "="* perc_count +">"+ " " * (10 - perc_count) + "] "
			+ " " + str(i).rjust(len(str(length))) + "/" + str(length)
			+ " | elapsed time "
			+ str(round(s, 2)).ljust(6, ' ') + "s", end='')
		yield each

def main():
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		sleep(0.005)
	print()
	print(ret)

if __name__ == "__main__":
	main()