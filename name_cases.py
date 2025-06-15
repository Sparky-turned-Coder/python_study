print("Please tell me your name. BEFORE IT'S TOO LATE!")
name = input().strip()
print(f"Hello, {name.title()}!")
print(f"Hello, {name.upper()}!")
print(f"Hello, {name.lower()}!")

print("Tell me your favorite video game right now.")
game = input()
print(f"{game.title().strip()} is a really great game.")