#! /usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/09 14:47:32 by darodrig          #+#    #+#              #
#    Updated: 2020/04/09 14:47:32 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import sys
import re
def main():
	if len(sys.argv) != 3 or not sys.argv[2].isdigit():
		print("ERROR")
		return
	n = int(sys.argv[2])
	if n == 0:
		return
	words = sys.argv[1].split(' ')
	words[:] = [re.sub("\W", '', each) for each in words]
	longwords = []
	for each in words:
		if len(each) > n:
			longwords.append(each)
	if len(longwords) == 0:
		print("ERROR")
	else:
		print(longwords)
	return

if __name__ == "__main__":
	main()