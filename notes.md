# Variables and Simple Data Types
- _Variables_ are boxes you can store data in.

- print(name.title())
    - title() is a _method_
- A _method_ is an action Python can perform on a piece of data.
    - The dot (.) after name tells python to make the title() method act on the variable 'name'.
- Methods are followed by parantheses () because they often need additional information to do their work.

* The title() method changes each word to _title case_, where each word begins with a capital letter.

Similarly, you can use _upper()_ and _lower()_ respectively to make all letters uppercase or all letters lowercase.

This is useful because you'll often want to think of a name as a piece of information. For example, you might want your program to recognize the input values Ada, ADA, and ada as the same name, and display all of them as 'Ada'.

The _lower()_ method is particularly useful for storing data. You typically won't want to trust the capatilzation that your users provide, so you'll convert strings to lowercase before storing them. Then when you want to display the information, you'll use the case that makes the most sense for each string.

## Using variables in Strings

- To insert a variable's value into a string, place the letter _f_ immediately before the opening quotation mark. Put braces around the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the string is displayed.
    - These are called _f-strings_. The _f_ is for _format_, because Python formats the string by replacing the name of any variable in braces with its value.



### Minor side track:
- Learned how strip(), lstrip, and rstrip() methods operate. Pretty neat.
    - rstrip() removes characters from the right (trailing) end of a string.
    - lstrip() removes characters from the beginning (left side) of the string.
    - strip() removes characters from both the beginning and end of a string.
        - By default (no arguement included), these methods remove whitespace characters (spaces, tabs, newlines, etc.). You can specify a string of characters to be removed as an arguement (inside the parantheses next to the method).

    - removesuffix() can be utilized to remove an exact phrase included in the arguement.
    - removeprefix() can be utilized to remove an exact phrase included in the argument.

### Methods we've run into thus far:
    - title()   - upper()   - lower()
    - rstrip()  - lstrip()  - strip()
    - removesuffix()    - removeprefix()

## Adding whitespace to strings with tabs and newlines
    - \n  will print the output on a new line
    - \t  will tab the output to the right

### Stripping Whitespace
We touched on this briefly above when I went on a side quest learning strip methods. Extra whitespace can be confusing in your programs. To programmers, "Python" and "Python " look the same, but to a program they are two _different_ strings. Python detects the extra whitespace and considers it significant unless you tell it otherwise.

