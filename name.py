# name = "ada lovelace"
# print(name.title())   

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(first_name)
print(last_name)
message = f"\tHello, {full_name.title()}!"  # We assigned the entire string to a new variable
print(message)              # And then we call a print function for that variable

# print("What is your name?")
# name = input()
# print(f"\tHello there, {name.title()}! \n\tPleasure to meet you!")

message = 'Monty Python'
print(message.rstrip(' Python'))

message = 'Monty D Python'
print(message.rstrip(' Python'))

# If you are wanting to just remove the exact word ' Python':   
name = 'Monty Python'
# if name.endswith(' Python'):
# name = message[:-len(' Python')]
# print(name)

# Or, more cleanly (Python 3.9+)
print(name.removesuffix(' Python'))

