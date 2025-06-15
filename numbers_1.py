import this

# import this  >>> generates Tim Peters' brief set of principles for writing good Python code.

# \n is not a function. It's an escape sequence that represents a line break character in a string. It can only be used with strings. So, in order to get this block of mathematical code to start on a new line, I assigned the first mathematical operation (5 + 3) to a variable, and then I printed that variable with \n.

addition = 5 + 3   
print(f"\n{addition}")
print(16 / 2)
print(2 ** 3)
print(10 - 2)
print(4 * 2)

print(f"\nWhat is your favorite number?")
fav_num = input()
print(f"You're favorite number is {fav_num.strip()}? That's my lucky number!")
