def get_multiply(start,end):
	ret = 1
	for num in range(start, end + 1):
		ret *= num
	return ret

a = int(input("start num>>"))
b = int(input("end num>>"))

print("{}부터 {}까지의 곱은 {}입니다.".format(a, b, get_multiply(a, b)))
