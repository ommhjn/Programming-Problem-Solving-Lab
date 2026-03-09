n=int(input("dimension: "))
A=[]
print("first matrix:")
for a in range(n):
	ra=list(map(int,input().split()))
	A.append(ra)
B=[]
print("second matrix:")
for b in range(n):
	rb=list(map(int,input().split()))
	B.append(rb)

result=[]
for r in range(n):
	result.append([0]*n)

for i in range(n):
	for j in range(n):
		for k in range(n):
			result[i][j]+=A[i][k]*B[k][j]

print("Resultant Matrix:")
for i in range(n):
	for j in range(n):
		if j==n-1:
			print(result[i][j],end="")
		else:
			print(result[i][j],end=" ")
	print()