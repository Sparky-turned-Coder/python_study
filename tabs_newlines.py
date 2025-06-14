# Tabs and Newlines
print("Languages: \n\tPython \n\tJavascript \n\tC++ \n\tRuby")

print("Work completed this week: \n\tFinished church steeple\n\tInvestigated highlands generator a bit more\n\tGot oil changed in work truck\n\tInstalled pendant lens at Mercy Healthcare\nGreat job!")

print("\nOrdered list nested inside an Unordered list in HTML: \n\tUL\n\t\tli\n\t\t\tOL\n\t\t\t\tli\n\t\t\t\tli\n\t\t\t\tli\n\t\t\t\tli\n\t\t\tOL\n\t\tli\n\t\tli\n\tUL")

# Stripping whitespace
print("What is your favorite programming language?")
fav_language = input()
print(f"Your favorite programming language is: {fav_language.strip().title()}. Great choice!")

github_url = 'https://www.github.com'
print(github_url) 
new_git_url = github_url.strip('https:// ')
print(f"Go to: {new_git_url} to reach GitHub.")