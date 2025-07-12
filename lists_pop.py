# Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)

# print(popped_motorcycle)

last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(f"\nThe last motorcylce I owned was a {last_owned.title()}.") 
print(f"\nThe first motorcyle I owned was a {first_owned.title()}.") 