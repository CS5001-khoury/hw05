# Homework 05 - Star Rating App

For this assignment, you are going to be building the skeleton of a more detailed
star rating app. This app will allow you to add movies and their ratings, and then
list them out. You will be making use of lists, tuples, and string manipulation in
addition to what you have already learned throughout the course.

## Implement the Functions
👉🏽 **TASK**:   Use the [star_rating_app.py](../star_rating_app.py).

Each function is detailed with expressive comments. You will also notice there are type hints in the file.

Let's work through an example:

```python
def convert_str_movie_tuple(val: str) -> Tuple[str, int]:
   """
    Converts a string in the format of "movie,rating" to a tuple
    It will clean up the title by calling clean_title, and will
    convert the rating to an int. This function assumes the string
    is correct, and in the format of "movie,rating" where movie is
    a string and rating is an int. 

    For Example:
        >>> convert_str_movie_tuple("v,5")
        ('V', 5)
        >>> convert_str_movie_tuple("Princess bride  ,10")
        ('Princess Bride', 10)
        >>> convert_str_movie_tuple("   JurAssic shARk  ,    1  ")
        ('Jurassic Shark', 1)

    Args:
         val (str): String in the format of "movie,rating"

    Returns:
        Tuple[str, int]: Movie and int rating 
   """
   pass
```


In the type hints, the contents in the brackets are the types inside the tuple or list. So Tuple\[str, int],
means a tuple with an string value, and int value should be returned. The capital "T" is something specific to type hints, as tuple is a specific command in python. 

Reading the comments, and looking at the examples, you see the function takes a string with a comma in it of the 
format (pattern) of "movie,rating". It then cleans up the title, and converts the rating to an int. You
do not have to do any error checking! That will come in a future assignment.  

### Building a list of tuples?

In this application you dealing with a list that is growing as more movies are added, but since the movie + rating doesn't change, those are tuples.

Here is an example of a running application:

```console
Welcome to the movie tracker!
Enter a movie and rating to add it to the list.
What would you like to do? add Princess Bride,10
What would you like to do? add Jurassic Shark,1
What would you like to do? add Corpse Bride, 5
What would you like to do? list
*****  Princess Bride
*      Jurassic Shark
*****  Corpse Bride
What would you like to do? exit
Thanks for using the movie tracker!
Sadly, movies will not be saved, as we still need to learn how to write to files.
```

The add commands would create an underlining structure of 

```python
[('Princess Bride', 10), ('Jurassic Shark', 1), ('Corpse Bride', 5)]
```

The list command then prints out every movie, with the star rating converting between 1 (min) and 5 (max) stars.
There is a specific format for the rating, which we provide in the comments how to do it!


### Filter
The hardest function is the `check_filter` function. It takes in a `(movie,rating)` along with a filter string. The filter string is a string that can be one of the following:
* '' - empty string, no filter
* 'any string' - any string, will return True if the movie contains the filter string. The `in` operator will help you! Case does not matter.
* 'operation value' - will filter the star rating based on the operation and the int value passed in. The operations are:
  * \> - greater than
  * < - less than
  * = - equal to
  * != - not equal to
  * \>= - greater than or equal to
  * <= - less than or equal to

The last one is the hardest case, as it means you have the check the first two characters of the filter string (removing spaces if they exist, as they will in the >, <, and = case), see if it is one of those operations, and then split the string based on the space. You will then take the first part of the split string to figure out which operation to use, and the second part to convert to an int to use
in the actual comparison (think a if/elif statement). You could also use the python [startswith](https://www.w3schools.com/python/ref_string_startswith.asp) method.


> Pro Tip / Highly Suggested  
> It is suggested you write the check_filter function  function increasing order of difficulty. For example, get the program running where the filter just always returns True. It won't work filtering, but you will have everything adding and printing. Then add the case where the filter is an empty string. Then add the case where the filter is a string for the movie title. Only after those cases are working, add the case where the filter is an operation. This will help you get the program working faster, and you can always go back and improve the code later. Incremental development like this is very common in programming, and successful programmers practice it all the time. 


#### Full example run with filters being used

```console
Welcome to the movie tracker!
Enter a movie and rating to add it to the list.
What would you like to do? add V,5
What would you like to do? add Princess Bride, 100
What would you like to do? add Corpse Bride,  5
What would you like to do? add jurassic shark, -10
What would you like to do? add Matrix  , 5
What would you like to do? add Matrix: Reloaded , 3 
What would you like to do? add Zombeaver,4
What would you like to do? list
*****  V
*****  Princess Bride
*****  Corpse Bride
*      Jurassic Shark
*****  Matrix
***    Matrix: Reloaded
****   Zombeaver
What would you like to do? list bride
*****  Princess Bride
*****  Corpse Bride
What would you like to do? list matrix
*****  Matrix
***    Matrix: Reloaded
What would you like to do? list >= 4
*****  V
*****  Princess Bride
*****  Corpse Bride
*****  Matrix
****   Zombeaver
What would you like to do? List = 4
****   Zombeaver
What would you like to do? list < 4
*      Jurassic Shark
***    Matrix: Reloaded
What would you like to do? list >= 1
*****  V
*****  Princess Bride
*****  Corpse Bride
*****  Matrix
***    Matrix: Reloaded
****   Zombeaver
What would you like to do? exit
Thanks for using the movie tracker!
Sadly, movies will not be saved, as we still need to learn how to write to files.
```

### Multiple Return Values?

In `menu()` you see we modified it to return two values. These two values are automatically converted to a tuple (see below if curious for details). This pattern is something that you will want to follow throughout your code. 


### Where to start?

1. Most of your functions can be written independently of each other (this was intentional in the design). As such, any of these functions are good starting points, and arguably the first ones you should write. Make sure to test after writing each one independently! 
   * clean_title - yes, this can be a single line function! 
   * convert_rating
   * check_filter - this is the hardest function, see the pro tip above
2. After you have clean_title working, you can write the convert_str_to_movie_tuple function. 
3. Once all the above is working, you have the components needed to work on `run()` and `print_movies()`.

While this is not the only path you can take when working on the functions, this is a possible one to consider. Remember, get an idea of the entire program the "big view", and then focus on the single task the function needs to do "small view". This assignment is much harder if you don't focus on the single task for each function!

#### Remember the mantra

1. Define
2. Document
3. Implement
4. Test



## Writing Tests

👉🏽 **TASK**: Using examples from past assignments, use [test_star_rating_app.py](../test_star_rating_app.py). 

You need to include two tests (ideally more) for every function *except* `menu()`, `run()`, and `print_movies(...)`. That is because every function besides those three are pure functions, meaning they do not have any side effects, and only return a value based on the input. We encourage you to think about your edge cases, and make sure you test those specifically. Eventually, you will not have an autograder for classes, so it is important to not rely on that testing for you. Instead, think about what specific conditions can be tested for each function, and write tests for those.

As with before, your new function should prepend test_, so the function that tests clean_title, should be `test_clean_title`.

## Part 3: README.md

👉🏽 **Task**: Answer the questions in the [README.md](../README.md) file. 

Make sure to answer the questions in the [README.md](../README.md) file.

As always you are free to ask about the questions in MS Teams, including clarifications on the code. 

## 📝 Grading Rubric

While we provide tests, reminder, you should test your own code before submitting!

1. Learning (AG)
   * clean_title with simple cases
   * convert_rating with simple cases
   * convert_str_to_movie_tuple with simple cases
2. Approaching  (AG)
   * clean_title with hard cases 
   * convert_rating with hard cases
   * convert_str_to_movie_tuple with hard cases
   * check_filter with no filter (empty string)
   * check_filter with string filter (title filter)
3. Meets  (AG)
   * check_filter with operation filter
   * print_list works for non-filtered and filtered
   * basic run is correct (exit only command)
   * run with multiple adds, lists, and then exit
   * passes pep8 style checker
4. Exceeds  (MG)
   * README.md questions answered
   * At least two test cases for all functions (except menu, run, and print_movies)
   * Proper comments and docstrings throughout code
   * Proper use of constants in code for star_rating_app (i.e. no typing out when a constant exists)


AG - Auto-graded  
MG - Manually graded



### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.

## 📚 Resources
* [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) - a number of useful methods to strings
* [Capwords](https://docs.python.org/3/library/string.html#string.capwords) - one option to generate title case
* [String Format Examples](https://docs.python.org/3/library/string.html#format-examples)
* [String Find Example](https://www.w3schools.com/python/ref_string_find.asp)
* [List Append Method](https://www.w3schools.com/python/ref_list_append.asp)
* [in/not in operator python](https://realpython.com/python-in-operator/)
  

### In Operator
To check for membership of a sequence (list, tuple, string, etc) you can use the `in` operator. For example

```python
if 'a' in 'abc':
   print("a is in abc") # this will print

if 5 in [1,2,3,4]:
   print("5 is in the list") # this will not print

if 'bride' in 'Princess Bride'.casefold():
   print("bride is in the title") # this will print, but only because of the casefold!
```

You can explore with the `in` operator in the python shell to see how it works.


### Multiple Return Types, Tuple?

In python, it is very common to have multiple values returned from a function. 
By default, a tuple is used to return the multiple values. As such, if we write the following function


```python

def my_func():
   return 10, 5

values = my_func()
print(values)
```
See [Visualization](https://pythontutor.com/render.html#code=def%20my_func%28%29%3A%0A%20%20%20return%2010,%205%0A%0Avalues%20%3D%20my_func%28%29%0Aprint%28values%29%0A%0A%23%23%20also%0Aprint%28values%5B0%5D%2B10%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

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
to the screen. See [Visualization](https://pythontutor.com/render.html#code=def%20my_func%28%29%3A%0A%20%20%20return%2010,%205%0A%0Aone,%20two%20%3D%20my_func%28%29%0A%0Aprint%28one%29%20%20%0Aprint%28two%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

The code is essentially saying

```python
values = my_func()

one = values[0]
two = values[1]
```

Needless to say, the automatic unpacking of values is easier to read in this case as long as you know the
exact number of return values.  Packing by default has a lot of uses. This [article on unpacking](https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/) has a lot of information (more than you need right now), but something to save to read for later. :relaxed:


