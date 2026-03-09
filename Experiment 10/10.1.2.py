def reverse_string(user_string):
	re=""
	l=len(user_string)
	for i in range (l-1,-1,-1):
		re += user_string[i]
	return re

user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")