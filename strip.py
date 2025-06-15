string = "  Hello World!  "

stripped_string = string.strip()    # "Hello World!"
lstripped_string = string.lstrip()  # "Hello World!   "
rstripped_string = string.rstrip()  # "   Hello World!"

print(f"Original string: '{string}'")
print(f"Stripped string: '{stripped_string}'")
print(f"Left-stripped string: '{lstripped_string}'")
print(f"Right-stripped string: '{rstripped_string}'") 

string2 = "!!!Hello World!!!"
stripped_string2 = string2.strip("!")  # "Hello World"
print(f"Original string2: '{string2}'")
print(f"Stripped string2 with exclamation point in arguement: '{stripped_string2}'")


