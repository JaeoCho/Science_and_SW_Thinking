def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else :
		return n * factorial(n-1)

cnt = 0

for i in range( 3, 1000001 ):
	sum_num = 0
	x = i
	while x != 0:
		sum_num += factorial(x % 10)
		x = x // 10
	if sum_num == i:
		cnt += 1
		print(i)

print(cnt)