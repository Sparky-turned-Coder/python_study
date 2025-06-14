print("What is your name ole buddy ole pal?")
name = input()
print(f"Nice to mee you, {name.title()}! Want to learn some python?")
answer = input("Please enter yes or no: ").lower().strip()
if answer == 'yes':
    print("Awesome!")
elif answer == 'no':
    print("Lame.")
else:
    print("That doesn't work buddy. 'Yes' or 'No' please and thank you.")
