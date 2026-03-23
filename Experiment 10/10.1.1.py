str=input()
char = ""
l=len(str)
for i in range(0,l):
	if str[i].isalnum() or str[i].isspace():
		char+=str[i]
print(char)