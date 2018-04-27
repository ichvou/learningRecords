#encoding: utf-8

def gcd(a,b):
	if not a>b:
		a,b=b,a

	while b != 0:
		re = a % b
		a,b=b,re

	return a

print(gcd(30, 40))
print(gcd(36, 12))

def lcm(a,b):
	return a*b / gcd(a, b)

print(lcm(30, 40))
print(lcm(36, 12))