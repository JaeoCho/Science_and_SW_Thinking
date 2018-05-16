boolean = 0

def find_min_square_root(n):
	global boolean
	start = 0
	end = n-1
	mid = 0
	while start < end:
		mid = int((start + end) / 2)
		if n <= mid ** 2:
			end = mid
			print(start, end)
		else:
			start = mid
			print(start, end)
	return mid

n = int(input())
print(find_min_square_root(n))
