# Homework 05 - Submission


* Student: YOUR NAME
* Semester: SEMESTER

## Common

* List any coding practice problems you completed, feel free to comment at needed (did it help, was it too easy, etc):

* List any other resources you used to help you complete the assignment (make sure to share good ones to the Tips,Tricks, and Resources channel in teams!):
  

## Module Specific

1 For each of the three sequential types you have learned (list, string, tuple) - label as mutable or immutable.

2. Explain mutability and immutability in your own words.

3. Given the following code:

```python
def mystery_function(x):
    x = 100

x = 1
print(x)
mystery_function(x)
print(x)
```

* What is the output of the code above?
  
* Explain why the output is what it is.


4. Given the following code:

```python
def mystery_function(x):
    x[0] = 100

x = [1, 2, 3]
print(x)
mystery_function(x)
print(x)
```
* What is the output of the code above? 

* Explain why the output is what it is.

5. Would happen if `x` was a tuple? What is generated when you try to run the code above with a tuple?


6. Given the following code:

```python
def mystery_function(x):
    x[1][0] = 100

x = (3, [1, 2, 3], [4, 5, 6])
print(x)
mystery_function(x)
print(x)
```

* What is the output of the code above?


## Deeper Thinking

The last bit of code is tricky. It is a tuple, which is immutable, but it contains a list, which is mutable. So, what happens when you try to change the list? Think about why this is the case, and make sure to think about the memory structure (and discuss it) as part of your example. We will discuss this in detail during the Module 06 team activity, but for now, we encourage you to just think about why this would be the case with what you have learned so far. It may help taking the above code, and running it through the python visualizer. 