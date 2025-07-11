# Python List Slicing

a = ['a', 'b', 'c', 'd', 'e']
print(a[2:])

a = [1, 3, 5, 7, 9]
print(a[1:])

a = ['a', 'b', 'c', 'd', 'e']
print(a[-2:-4:-1])      # Here we are slicing the list 'a' from index -2 to -4, with a step of -1

#   a =    ['a', 'b', 'c', 'd', 'e']
# Indexes:   0    1    2    3    4
# Negative: -5   -4   -3   -2   -1

# This means:

# Start at index -2 → 'd'

# Stop before index -4 → 'b'

# Step -1 → move backward one element at a time

# b =   0           1               2            3      4

gaming_systems = ['xbox', 'playstation', 'nintendo switch', 'pc', 'mobile']
print(gaming_systems[1:3:2])

