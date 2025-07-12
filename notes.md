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
    - rstrip() removes characters/whitespace from the right (trailing) end of a string.
    - lstrip() removes characters/whitespace from the beginning (left side) of the string.
    - strip() removes characters/whitespace from both the beginning and end of a string.
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

### Underscores in Numbers
When you're writing long numbers, you can group digits using underscores to make large numbers more readable:  

    >>> universe_age = 14_000_000_000 years old  

When you print a number that was defined using underscores, Python prints only the digits:   

    >>> print(universe_age)  
     14000000000 years old  

### Integers and Floats
When you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float:  

    >>> 4/2  
     2.0  

If you mix an integer and a float in any other operation, you'll get a float as well:  

    >>> 1 + 2.0  
     3.0  
    >>> 2 * 3.0  
     6.0  
    >>> 3.0 ** 2  
     9.0  

### Multiple Assignment
You can assign values to more than one variable using just a single line of code. This can help shorten your programs and make them easier to read; you'll use this technique most often when initializing a set of numbers.  

    >>> x, y, z = 1, 2, 3  
    >>> print(x)  
     1  
    >>> print(y)  
     2  
    >>> print(z)  
     3  
    >>> print(x, y, z)  
     1 2 3  

*** I tested multiple assignment with assigning string values to variables, and it works, just not sure yet when this will come into practical use. We shall see.

### Constants
A _constant_ is a variable whose value stays the same throughout the life of a program. _Python doesn't have built-in contant types_, but Python programmers use all capital letters to inidicate a variable should be treated as a constant and never be changed. (good python syntax etiquette to know)  
    >>> MAX_CONNECTIONS = 5000  

So when you want to _treat_ a variable as a constant in your code, write the name of the variable in all capital letters. This reminds you that it was intended to be a constant in case you forget, and allows other programmers who view your code to know the same thing.

### The Zen of Python
Enter _import this_ into a Python terminal session to view Tim Peters' brief list of principles for writing good Python code. 

# Introducing Lists
### List slicing
Skipping ahead here because I ran into a python challenge question on LinkedIn last night that peaked my interest. Now I want to understand how slicing a list works (I'm just starting the chapter on lists).  

    >>> a = ['a', 'b', 'c', 'd', 'e']
    >>> print(a[-2:-4:-1])      # Here we are slicing the list 'a' from index -2 to -4, with a step of -1  

    >>> a =    ['a', 'b', 'c', 'd', 'e']  
    Indexes:     0    1    2    3    4  
    Negative:   -5   -4   -3   -2   -1  

This means:  

Start at index -2 → 'd'  

Stop before index -4 → 'b'  

Step -1 → move backward one element at a time 

### Using individual values in a list
You can use individual values fro ma list just as you would any other variable. For example, you can use F-strings to create a message based on a value from a list.
    See:  lists.py

We build a sentence using the value at bicycles[0] and assign it to the variable message. The output is a simple sentence about the first bicycle in the list.

### Using Enumerate()
If you need to see index assignments for values you've assigned to a list variable, you can use this function to print out the index number and the value to see exactly what index each item in your list is.

_for index, item in enumerate(mylist):_
This is a for loop header. Several things happen here:

_for ... in ...:_	Tells Python to iterate over a sequence, executing the indented block once for each element.
_enumerate(mylist)_	The built‑in enumerate() function wraps any iterable and yields pairs (index, value) on the fly:
[(0, 'apple'), (1, 'banana'), (2, 'cherry'), …]. By default the index starts at 0, but you can pass a start argument (e.g., enumerate(my_list, start=1)).
_index, item_	Tuple unpacking. Each (index, value) pair produced by enumerate() is a two‑element tuple. The first element is assigned to index, the second to item on every iteration.

So the loop runs three times with these variable bindings:

    Iteration index	item
      1	      0	    'apple'
      2	      1	    'banana'
      3	      2	    'cherry'

Then, we just _print(index, item)_ to see the result.

### Range()
When using range(), we create a sequence of numbers starting at 1 and stopping _before_ 5.

    for i in range(1, 5):
        print (i)

Will output:

    1
    2
    3
    4

The number 5 is _excluded_ - that's how range() works in Python:
    range(start, stop) → includes start, excludes stop

