# Homework 05 - Refactoring Star Rating

For this 


Assignment description here

Highlight each major component with a section, add **task** for tasks and include 👉🏽 or something obvious so they can be found easily. 



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
* [String format examples](https://docs.python.org/3/library/string.html#format-examples)
* [String Find Example](https://www.w3schools.com/python/ref_string_find.asp)
  
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
