string = "  Hello World!  "

stripped_string = string.strip()    # "Hello World!"
lstripped_string = string.lstrip()  # "Hello World!   "
rstripped_string = string.rstrip()  # "   Hello World!"

print(f"\nOriginal string: '{string}'")
print(f"Stripped string: '{stripped_string}'")
print(f"\n\tLeft-stripped string: '{lstripped_string}'")
print(f"\tRight-stripped string: '{rstripped_string}'") 

string2 = "!!!Hello World!!!"
stripped_string2 = string2.strip("!")  # "Hello World"
print(f"\nOriginal string2: '{string2}'")
print(f"Stripped string2 with exclamation point in arguement: '{stripped_string2}'")

# Let's try stripping, tabbing, and newlining with something else

game = '    nintendo wii     '
game_two = '    sony playstation'
game_three = 'microsoft     xbox'

stripped_game = game.strip()
lstripped_game_two = game_two.lstrip('sony ')
rstripped_game_three = game_three.rstrip(' xbox')

print(f"\n\tGame: {game}")
print(f"\tGame 2: {game_two}")
print(f"\tGame 3: {game_three}")

print(f"\n\t\tStripped game: {stripped_game}")
print(f"\t\tLeft-stripped game 2: {lstripped_game_two}")
print(f"\t\tRight-stripped game 3: {rstripped_game_three}")
