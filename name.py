# name = "ada lovelace"
# print(name.title())   

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(first_name)
print(last_name)
print(f"Hello, {full_name.title()}!")

print("What is your name?")
name = input()
print(f"Hello there, {name.title()}! Pleasure to meet you!")

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


