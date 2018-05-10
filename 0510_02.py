def convert(num,m) :
	if num < m:
		if num >= 10:
			return chr(num + 55)
		else:
			return chr(num + 48)

	else :
		if num % m >= 10:
			return convert(num // m, m) + chr ((num % m) + 55)
		else:
			return convert(num // m, m) + chr((num % m) + 48)

n = int(input("숫자"))
c = int(input("진법"))
print(convert(n,c))
