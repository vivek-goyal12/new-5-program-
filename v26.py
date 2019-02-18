str = input("enter a string")
name =""
for i in range(0,len(str)):
	name = str[i] + name
#print(name)
if name==str:
	print("yes")
else:
	print("No")
