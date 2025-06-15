file_one = 'notes.txt'
file_two = 'dark souls.jpeg'
file_three = 'stripping names.py'
file_four = 'monster.js'

print(f"\n{file_one}")
print(file_two)
print(file_three)
print(file_four)

print(f"\nHere's the list of files you were searching for without the extensions: {file_one.removesuffix('.txt')}, {file_two.removesuffix('.jpeg')}, {file_three.removesuffix('.py')}, {file_four.removesuffix('.js')}")

print(f"\nHere's the list of extensions the above files utilize: {file_one.removeprefix('notes')}, {file_two.removeprefix('dark souls')}, {file_three.removeprefix('stripping names')}, {file_four.removeprefix('monster')}")

filename = 'python_notes.txt'
print(f"\nLastly, here's the file you needed for your notes, minus the extension: {filename.removesuffix('.txt')}")
print(f"The file extension used was: {filename.removeprefix('python_notes')}")
