#! /usr/bin/env python3
import datetime

def main():
	v = (3, 30, 2019, 9, 25)
	t = datetime.datetime(v[2], v[3], v[4], v[0], v[1])
	print(t.strftime("%m/%d/%y %H:%M"))

if __name__ == "__main__":
	main()