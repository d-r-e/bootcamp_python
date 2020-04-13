#!/usr/bin/env python3
from vector import Vector

if __name__ == "__main__":
	v = Vector([-0.2, 3, 4])
	print(v)
	v = Vector(5)
	print(v)
	v = Vector(-15, -19)
	print(v)
	w = 6 + v
	print(w + (-5))
	x = 5 - Vector(4)
	print(x)
	print()
	x = Vector(4) * 2
	otro = x + 1
	print("otro", otro)
	x = 0 / otro
	print(x)
	x = Vector([1, 0]) * Vector([0, 2])
	print(x)

	print(repr(Vector(4)))