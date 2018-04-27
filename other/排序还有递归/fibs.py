#encoding: utf-8

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

def fib1(n):
	if n <= 2:
		return n
	else:
		return fib1(n-1) + fib1(n-2)


def fib2(n):
	a,b=0,1
	for _ in range(n):
		a,b=b,a+b
	return b

fib3 = lambda n: n if n < 2  else 2 * fib3(n-1)	

print(fib(10))
print(fib1(10))
print(fib2(2))
print(fib3(10))

for c in range(0,10,2):
	print(c)
