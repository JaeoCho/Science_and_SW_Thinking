import time
import sys
sys.setrecursionlimit(10000000)

counter = 0

def fibo (n):
	global counter
	counter += 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else :
		return fibo(n-1) + fibo(n-2)


a = int(input())
start_time = time.time()
b=fibo(a)
all_time = time.time() - start_time
print(b, all_time)

fibo_num = []
fibo_num.append(0)
fibo_num.append(1)

start_time = time.time()
for i in range (2,a+1):
	fibo_num.append(fibo_num[i-1] + fibo_num[i-2])
all_time = time.time() - start_time
print(fibo_num[a], all_time)