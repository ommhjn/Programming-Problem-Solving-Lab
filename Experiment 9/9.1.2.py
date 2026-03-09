inp = input()
flag = True
l=len(inp)
for i in range(l):
	if inp[i]!=inp[l-1-i]:
		flag = False
if flag:
	print("Palindrome")
else:
	print("Not a Palindrome")