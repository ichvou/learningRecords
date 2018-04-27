#encoding: utf-8

valueStr=input("saa:")
try:
	if valueStr.isdigit():
		valueInt=int(valueStr)
	else:
		raise (ValueError,valueStr)
except ValueError:
	print("cao!",valueStr)