import time
input = input("Enter the text >>> ")
x = str()
for n in input:
	x += n
	print(x,end="\r")
	time.sleep(0.5)