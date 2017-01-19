class BinarySeach(list):
	def __init__(self, a, b):
		self.a = len(list)
		self.b = step
		self.length = len(array)
	def Search(find_val):
		first = 0
		last = self.a - 1
		found = False

		while first <= last and not found:
			mid_point = (first + last)//2
			if list[mid_point] == find_val:
				found = True
			else:
				if find_val < list[mid_point]:
					last = mid_point - 1
				else:
					first = mid_point + 1
		return found