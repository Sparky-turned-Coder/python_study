family = ['Chris', 'Lyndsey', 'Emma', 'Nana', 'Papa', 'Alaina']
print(family[1])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[2].title())
print(bicycles[1])
print(bicycles[0].upper())
print(bicycles[-1])  # If you ask for the item at index -1, Python always returns the last item in the list. Index -2 returns the second to last item in the list. Index -3 returns the third to last item in the list, and so on.

# Use an f-string to create a message based on a value from a list.
message = f"\nMy first bicycle was a {bicycles[0].title()}."
print(message)

# Try it youself exercise: page 36

names = ['christian', 'lyndsey', 'nick', 'kyle', 'jeff']
print(names[-1].title())
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

message = f"\nWhat's up {names[0].title()}?"
message1 = f"\nI love you {names[1].title()}!"
message2 = f"\nYou're gay, {names[2].title()}."
message3 = f"\nWe are brothers from the same mother, {names[3].title()}."
message4 = f"\n{names[4].title()} and I used to work together at Harlan."

print(message)
print(message1)
print(message2)
print(message3)
print(message4)

games = ['Expedition 33', 'Final Fantasy IX', 'Elden Ring', 'Pokemon']

mes1 = f"\nI love {games[0]} because it brings me back to the old style turn based combat. And the story is A+!"
mes2 = f"\n{games[1]} is my all-time favorite Final Fantasy game. The story, the characters. Chef's kiss. (pun intended Quina)"
mes3 = f"\nI have spent an absurd amount of time playing {games[2]}. According to Xbox, 45 days to be exact. Pretty sure that's more than any game I've ever played. 45 multiplied by 24, I don't even want to know how many hours I put into this game."
mes4 = f"\nGrowing up, {games[3]} was the goat. I played it so much it's insane. All of the Pokemon games combined are more hours than {games[2]}."

print(mes1)
print(mes2)
print(mes3)
print(mes4)