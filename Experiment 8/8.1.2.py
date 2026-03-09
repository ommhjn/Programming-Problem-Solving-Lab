start = int(input())
stop = int(input())

found = 0

for n in range(start, stop+1):
	if n > 1:
		for i in range(2, n):
			if n % i == 0:
				break
		else:
			print(n)
			found = 1

if found == 0:
	print("No primes")