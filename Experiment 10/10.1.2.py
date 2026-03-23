def reverse_string(user_string):
	result=""
	l=len(user_string)
	for i in range (l-1,-1,-1):
		result += user_string[i]
	return result
user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")