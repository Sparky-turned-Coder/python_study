# Variables and Simple Data Types
- _Variables_ are boxes you can store data in.

- print(name.title())
    - title() is a _method_
- A method is an action Python can perform on a piece of data.
    - The dot (.) after name tells python to make the title() method act on the variable 'name'.
- Methods are followed by parantheses () because they often need additional information to do their work.

* The title() method changes each word to _title case_, where each word begins with a capital letter.

Similarly, you can use _upper()_ and _lower()_ respectively to make all letters uppercase or all letters lowercase.

This is useful because you'll often want to think of a name as a piece of information. For example, you might want your program to recognize the input values Ada, ADA, and ada as the same name, and display all of them as 'Ada'.

The _lower()_ method is particularly useful for storing data. You typically won't want to trust the capatilzation that your users provide, so you'll convert strings to lowercase before storing them. Then when you want to display the information, you'll use the case that makes the most sense for each string.

