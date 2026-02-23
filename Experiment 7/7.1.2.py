a,b,c=input().split()
digits=[a,b,c]
for a in range(3):
	for b in range(3):
		for c in range(3):
			if a!=b and b!=c and c!=a:
				print(digits[a]+digits[b]+digits[c])