inp=input()
char = ""
for i in inp:
	if i.isalnum() or i.isspace():
		char+=i
print(char)