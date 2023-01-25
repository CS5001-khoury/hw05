# Homework 05 - Refactoring Star Rating

[Refactoring] and Testing code are some of the first jobs many programmers get (often as interns). That is because it gives you the opportunity to see both bad and good code, and to help you figure out better ways to work the code (or set it up for future enhancements). 

For this assignment, you will be refracting your old Star Rating code, along with adding new functionality (features!). We hope the moment you started learning about lists, you started to reflect on this assignment. It was designed to use lists. 

While this weeks assignment is only going to focus on Star Rating App, don't let yourself fall behind. There are a lot of nuances you are learning. 

## Implement the Functions
👉🏽 **TASK**   Use the [star_rating_app.py](star_rating_app.py) as a template to update star rating. You are free to pull old functions from Homework 04, and add additional functions if it helps you. Be careful and intentional about what you copy over! You don't want to introduce errors by accident. 

Each function is detailed with expressive comments. You will also notice there are type hints in the file.

Let's work through an example:

```python
def add_movie(val : str = '') -> Tuple[str, int]:
    """
    Gets a movie and rating from the client.
    if not input is provided, get_movie_by_input()
    is called with its values returned.

    
    For Example:
        >>> add_movie("v,5")
        ('V', 5)
        >>> add_movie("Princess bride  ,10")
        ('Princess Bride', 10)
        >>> add_movie("   JurAssic shARk  ,    1  ")
        ('Jurassic Shark', 1)

        assume avatar and 3 are entered
        >>> add_movie()              # doctest: +NORMALIZE_WHITESPACE
        Enter a movie:
        Enter a rating 1-5: 
        ('Avatar', 3)

    Args:
        val (str, optional): movie to add if provided as a commas separated value. Defaults to ''.

    Returns:
        Tuple[str, int]: Movie and int rating 
    """
    return '', 0 # replace
```

This says, add_movie can now take an optional string argument. If the string is empty or not provided, then it will
use the get_movie_by_input() function, returning the results.  If a string is provided, you can
assume there is a comma, and split on that string. You will also want to look at `clean_title(str) -> str`.

In the type hints, the contents in the brackets are the types is side the tuple or list. 

### Building a list of tuples?

In this application, instead of building a string separated by new lines, you are building a list of tuples

For example, the following input into the console
```text
What would you like to do? v,5
What would you like to do? Jurassic Shark , 1
What would you like to do? Jurassic Park, 3
What would you like to do? It's a wonderful life,4
```
Would create an underline structure of

```python
[('V', 5), ('Jurassic Shark', 1), ('Jurassic Park', 3), ("It's a wonderful life", 4)]
```

That structure (a List[Tuple[str, int]]) would be passed into `print_movie(movies)`, when then loops
through the list, and converts the `int` part of the tuple to stars using your  `convert_rating(val: int) -> str` which can be taken from Homework 04. 

The output of the list above should look like the following:

```text
*****  V
*      Jurassic Shark
***    Jurassic Park
****   It's A Wonderful Life
```

Making a complete run look like:


```console
What would you like to do? v,5
What would you like to do? Jurassic Shark , 1
What would you like to do? Jurassic Park, 3
What would you like to do? It's a wonderful life,4
What would you like to do? list
*****  V
*      Jurassic Shark
***    Jurassic Park
****   It's A Wonderful Life
What would you like to do? exit
```

> Notice that spacing matters now! We will not be removing spaces in the tests, so you will want to review string format. 

### Multiple Return Values?

In `menu()` you see we modified it to return two values. These two values are automatically converted to a tuple (see below if curious for details). This pattern is something that you will want to follow throughout your code. 


### Where to start?

1. Often when you refactor, you start with what you are not going to change. In this case, two functions will remain the same from Homework 04. 
   * get_valid_int(prompt: str) -> int
   * convert_rating(val: int) -> str
2. Then start at the simplest function that can tested individually.  Good targets are
   * clean_title(str) -> str
3. Then build up from there, so maybe add_movie, and just see if you can make the tuple.

The question then goes how can you test all this, if the main program isn't running yet?

## Writing Tests

👉🏽 **TASK** Using examples from past assignments, create test_star_rating.py. At the bare minimum you should include tests for
* clean_title
* convert_rating
* add_movie

But it is possible to test every function. Just include in the comments the input/output you expect. 

As with before, your new function should prepend test_, so the function that tests clean_title, should be `test_clean_title`.

## Final Step: Reflect

This assignment will take some research and looking up tutorials (though the resources below are good places to start). Refactoring code has a very different feeling than building code from scratch. What are some of your thoughts and feelings of this application as it grows? What are some features you would like to see in the future? What features would you expect to see.

In addition to answering the above prompt in your README.md, please take a moment to describe the differences between mutable and immutable. Can you use code examples as part of your description. 

Understanding how immutable works, why do you think python would default to return tuples when more than one value is returned as compared to returning lists? 

As a reminder, you are free to ask these questions on MS Teams, as long as you further the questions with thoughts and discussions. Concepts are free game for chatting (just don't cut and past others answers) :) 

## 📝 Grading Rubric


Add (AG) and (MG) next to tiers, add major conditions to meet to pass each tier. 

1. Learning ()
   * 
2. Approaching  ()
   * 
3. Meets  ()
   * 
4. Exceeds  ()
   * 


AG - Auto-graded  
MG - Manually graded


## 📚 Resources
* [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) - a number of useful methods to strings
* [Capwords](https://docs.python.org/3/library/string.html#string.capwords) - one option to generate title case
* [String Format Examples](https://docs.python.org/3/library/string.html#format-examples)
* [String Find Example](https://www.w3schools.com/python/ref_string_find.asp)
* [List Append Method](https://www.w3schools.com/python/ref_list_append.asp)
  
### Multiple Return Types, Tuple?

In python, it is very common to have multiple values returned from a function. 
By default, a tuple is used to return the multiple values. As such, if we write the following function


```python

def my_func():
   return 10, 5

values = my_func()
print(values)
```

the values `(10, 5)` would be printed as the tuple. You can also access items in that tuple.

```python
print(values[0]+10)
```
Would cause `20` to be printed. 

#### Adding Unpacking

It is also common to 'unpack' values, especially from function returns.

```python
one, two = my_func()

print(one)  
print(two)
```
would print
```
10
5
```
to the screen. 

The code is essentially saying

```python
values = my_func()

one = values[0]
two = values[1]
```

Needless to say, the automatic unpacking of values is easier to read in this case as long as you know the
exact number of return values.  Packing by default has a lot of uses. This [article on unpacking](https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/) has a lot of information (more than you need right now), but something to save to read for later. :relaxed:


[Refactoring]: https://en.wikipedia.org/wiki/Code_refactoring