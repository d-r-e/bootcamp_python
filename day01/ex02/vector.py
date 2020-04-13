class Vector(object):
	def __init__(self, *args):
		try:
			self.values = []
			if len(args)==1 and type(args[0])==int and args[0]>0:
				for n in range(args[0]):
					self.values.append(float(n))
				self.size = args[0]
			elif type(args[0]) == list and len(args[0]) > 0:
				for n in args[0]:
					self.values.append(float(n))
				self.size = len(self.values)
			elif type(args[0])==int and type(args[1]) == int and args[0] != args[1]:
				if args[0] > args[1]:
					step = -1
				else:
					step = 1
				for n in range(args[0], args[1], step):
					self.values.append(float(n))
				self.size = len(self.values)
			else:
				raise ValueError
		except ValueError:
			print("Error: Wrong vector initialization")
	
	def __str__(self):
		txt = "(Vector "
		txt += "".join(str(self.values)) + ")"
		return txt
	
	def __repr__(self):
		txt = "{" + "values: " + str(self.values) \
				+ ", size: " + str(self.size) + "}"
		return txt

	def __add__(self, v):
		try:
			if type(v) == int:
				values = []
				for n in self.values:
					values.append(n + v)
				return(Vector(values))
			if len(self.values) != len(v.values):
				raise IndexError
			values = []
			for n in range(self.size):
				values.append(self.values[n] + v.values[n])
			return (Vector(values))
		except IndexError:
			print("Error: vectors are not the same size")

	def __radd__(self, v):
		return(self + v)
	
	def __sub__(self, v):
		try:
			if type(v) == int:
				values = []
				for n in self.values:
					values.append(n - v)
				return(Vector(values))
			if len(self.values) != len(v.values):
				raise IndexError
			values = []
			for n in range(self.size):
				values.append(self.values[n] - v.values[n])
			return (Vector(values))
		except IndexError:
			print("Error: vectors are not the same size")

	def __rsub__(self, v):
		return(self - self - self + v)
	
	def __truediv__(self, v):
		try:
			values = []
			for n in self.values:
				values.append(n / v)
			return(Vector(values))
		except ZeroDivisionError:
			print("Error: non divisible by 0")
		except TypeError:
			print("Error: wrong type")

	def __rtruediv__(self, v):
		try:
			values = []
			for n in self.values:
				values.append(v / n)
			return(Vector(values))
		except ZeroDivisionError:
			print("Error: non divisible by 0")
		except TypeError:
			print("Error: wrong type")

	def __mul__(self, value):
		try:
			if type(value) == Vector:
				if self.size != value.size:
					raise IndexError
				result = 0
				for n in range(self.size):
					result += self.values[n] * value.values[n]
				return result
			values = []
			for each in self.values:
				values.append(each * value)
			return Vector(values)
		except IndexError:
			print("Error: mismatching vector length")
		except TypeError:
			print("Error: multiplying wrong type")
	
	def __rmul__(self, value):
		return self * value