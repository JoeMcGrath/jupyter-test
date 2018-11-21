#!/usr/bin/env python
# coding: utf-8

# # Python 101
# Introduction to Python / Python reference
# 
# This has been written specifically for Python 2.7
# 
# You can find the official Python documentation here: https://docs.python.org/2.7/

# ## Contents
#     0. Hello, world!
#     1. Variables & Types
#         1.1 Numbers
#         1.2 Strings
#         1.3 Booleans
#         1.4 Lists
#         1.5 Dictionaries
#     2. Comparisons
#         2.1 If/Else
#         2.2 Comparison Operators
#         2.3 Ternary Operators
#     3. Loops
#         3.1 For Loops
#         3.2 While Loops
#         3.3 Other Iterables
#     4. Functions
#         4.1 Declaring Functions
#         4.2 Parameters
#         4.3 Default parameters
#         4.4 Recursion
#     5. Libraries
#         5.1 Importing Modules
#         5.2 Local/Custom Modules
#         5.3 External Dependencies
#     6. Miscellaneous
#         6.1 Exceptions
#         6.2 Reading and Writing to Files
#         6.3 Data Visualisation
#         6.4 HTTP Requests
#         6.5 Numpy

# ## 0. Hello, world!
# Welcome to the Python 101 for A.I.Camp! This will give you a crash course in the basics of Python, getting you set up with all you need to know before we start getting into machine learning!
# 
# You can also use this as a reference when you need help with syntax.
# 
# Let's start with a basic "Hello, world!"
# 
# *Hint: In Jupyter Notebooks, you can click on a piece of code and hit **shift+enter** to run it! Any output will be displayed below the code.*

# In[2]:


print ('Hello, world!')


# While we're at it, comments in Python use the hash (#) symbol.

# In[3]:


# I'm a comment!


# ## 1. Variables & Types
# The five main variable types we'll look at are:
# - **Numbers** (ints, floats)
# - **Strings**
# - **Booleans** (true/false)
# - **Lists** (known as arrays in other languages)
# - **Dictionaries** (similar to objects in other languages)
# 
# Python is dynamically typed, meaning variables are declared **without** specifying a type.

# In[4]:


number_example = 101
string_example = 'A.I. is coool'
boolean_example = True
list_example = [2, 4, 6, 8]
dictionary_example = {
    'id': 1,
    'colour': 'yellow'
}


# To find out a variable's type, we run the `type` function on it:

# In[6]:


print (type(number_example))
print (type(string_example))


# An object's type can also be changed after it is created:

# In[8]:


# Set a to be a number
a = 1
print (type(a))

# Set a to be a string
a = 'Test'
print (type(a))


# ### 1.1 Numbers

# When we talk about numbers in Python, we generally mean integers, but it could also mean floats.

# In[10]:


a = 3
print (a)
print (type(a))

b = 1.5
print (b)
print (type(b))


# #### Operators
# Numbers can be manipulated with several standard mathematical operations.

# In[11]:


print (a + 1)  # Addition
print (a - 4)  # Subtraction
print (a * 5)  # Multiplication
print (a / 3)  # Division
print (a ** 2) # Exponentiation
print (a % 2)  # Modulus


# There's no `x++` in Python. Instead, we can do `x += 1`.

# In[12]:


b = 5
b += 1
print (b)


# #### Casting
# An integer can be cast as a float and vice versa. Simply pass the integer into the `float` function.

# In[13]:


print (float(20))


# Python quirk: If you divide two integers, the result will be an integer...

# In[14]:


a = 5
b = 2
print (a / b)


# To get around this, we can cast one of the integers to a float. This will force the result to also be a float.

# In[15]:


print (float(a) / b)


# #### Formatting
# Sometimes when printing a float, we want to format it in a specific way - e.g. currencies typically are written to two decimal places. Use the following syntax to format a float:

# In[16]:


d = 2.543
print ('{:.2f}'.format(d)) # Print d to two decimal places


# ** Random **
# 
# Python makes it very easy to generate random numbers. Below is the syntax for generating an int between 1 and 6 (inclusive).

# In[17]:


import random
dice_value = random.randint(1, 6)
print (dice_value)


# More commonly, you may need to generate a random float between 0 and 1:

# In[18]:


r = random.random()
print (r)


# ### 1.2 Strings

# Strings in Python can use either single (') or double (") quotes. Normally developers use single quotes, but whatever you choose - stick with it and be consistent!

# In[19]:


s = 'Kainos'
s2 = "Kainos"

print (type(s))
print (type(s2))


# To get the length of a string, we can use the `len` function:

# In[21]:


print (s)
print (len(s))


# #### Appending strings
# Strings can be appended using the `+` operator:

# In[22]:


base_string = 'The string is: '
keyword = 'A.I.'

print (base_string + keyword)


# However, there is a more preferred/safer way to do this using the `%s` and `%` format to insert strings into other strings. For example:

# In[23]:


base_string = 'The string is: %s' # %s signifies where to insert a string
keyword = 'A.I.'

print (base_string % keyword)


# New lines can be inserted with `\n`

# In[24]:


print ('Hello\nNew line')


# **Numbers and strings**
# 
# Variables of differing types typically can't be appended to one another. Int the case of numbers and strings, numbers must be cast to a string so that it can be appended.

# In[25]:


a = 1
s = 'The number is: '
print (s + str(a))


# Alternatively, `%d` can be used for inserting numbers into strings

# In[26]:


a = 1
s = 'The number is: '
print ('%s%d' % (s, a))


# ### 1.3 Booleans

# Python's booleans are capitalised.

# In[27]:


t = True
f = False
print (type(t))


# You can perform the standard boolean operations on them.

# In[29]:


print (t and f) # AND
print (t or f)  # OR
print (not t)   # NOT
print (t != f)  # XOR


# ### 1.4 Lists
# Lists are Python's equivalent of arrays in many other languages.

# In[30]:


l1 = [1, 2, 3]
print (l1)
print (type(l1))


# To get the length of a list, use the same function as for strings: `len`.

# In[31]:


l1 = [1, 2, 3]
print (len(l1))


# **List indexes**
# 
# Similar to many other languages, access to an item within a list uses square brackets. The index starts at 0.

# In[32]:


l1 = [1, 2, 3]
print (l1[0]) # Accessing the value at position 0


# Python also has a cool feature where you can use a negative index to get an item from the end of a list. `-1` is the last element, `-2` the second last, and so on.

# In[33]:


l1 = [1, 2, 3]
print (l1[-1]) # Accessing the value at the last position


# ** Modifying lists **
# 
# In many languages, lists/arrays have a fixed length once set. In Python, lists can be dynamically resized.

# In[34]:


l2 = ['hello']
l2.append('world')
print (l2)


# Lists can be appended to other lists

# In[35]:


print ([1, 2, 3] + [4, 5, 6])


# **Types & nested lists**
# 
# Lists can contain different types of objects

# In[36]:


l3 = [1, 'hello', False]
print (l3)


# Lists can also be nested

# In[37]:


l4 = [
    ['oranges', 'bananas'],
    ['chocolate', 'crisps', 'cake']
]


# **Splitting lists**
# 
# Python lists can be split up into "sub" lists, for example `[1, 2, 3, 4, 5]` could be split into `[1, 2, 3]` or `[2, 3, 4, 5]` etc.
# 
# The notation used `[x:y]`, where `x` is the index of the start of the range, and `y` is the index **after** the last item in the range.

# In[38]:


l5 = ['a', 'b', 'c', 'd', 'e', 'f']
print (l5[0])   # First element of l5
print (l5[0:2]) # First two elements of l5
print (l5[1:3]) # Second and third elements of l5


# A blank index on the left of `:` indicates the start of the list (i.e. 0). A blank index on the right indicates the end of the list.

# In[39]:


print (l5[:2])  # Alternative notation for first two elements
print (l5[1:])  # All elements except for the first
print (l5[:])   # All elements of l5


# Combining this with negative indexes can be very powerful!

# In[40]:


print (l5[:-1]) # All elements except for the last
print (l5[-2:]) # The last two elements in the list


# **Zip**
# 
# Python has a built-in zip function that pairs up values in multiple lists.
# 
# For example, zipping the two lists `[1, 2, 3]` and `['a', 'b', 'c']` will result in `[(1, 'a'), (1, 'b'), (3, 'c')]`.

# In[43]:


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print (zip(list1, list2))


# These values pairs are called **tuples**.
# 
# can zip together as many lists as you want.

# In[44]:


list3 = [10, 11, 12]
list4 = [True, True, False]
print (zip(list1, list2, list3, list4))


# You can zip different sizes of lists, but the number of tuples created will only be as many as the shortest list.

# In[45]:


list5 = [100, 200, 300, 400]
zip(list4, list5)


# ### 1.5 Dictionaries
# Think of dictionaries like objects with properties. We can create dictionaries in Python using a **key: value** notation.

# In[ ]:


person = {
    'name': 'George',
    'age': 21
}
print person
print type(person)

print person['name'] # Access the value of the key/property 'name'

person['location'] = 'Belfast' # Dictionaries can have new properties added to them
print person


# ## 2. Comparisons

# Python has the usual if/else features.
# 
# There are a couple of things to note:
# - The "else if" notation is `elif`
# - In Python we don't use curly brackets. Instead we use colons (:) and indentation. Nested code should be four spaces (or one tab character) to the right of its parent.

# ### 2.1 If/Else
# 
# The following is the general syntax structure for an if/else if/else in Python:

# In[ ]:


a = 5
if a > 0:
    print 'positive'
elif a < 0:
    print 'negative'
else:
    'zero'


# ### 2.2 Comparison Operators
# 
# There are several comparison operators you may need to use for comparing variables to one another.

# In[ ]:


a = 3
b = 5

a == b     # Equality
a > b      # Greater than
a < b      # Less than
a >= b     # Greater than or equal to
a <= b     # Less than or equal to
a != b     # Not equal to
a is b     # Alternative equality
a is not b # Alternative not equal to


# For booleans, we don't need to check for equality...

# In[ ]:


turned_on = True

if turned_on == True:
    print 'Turned on'

if turned_on:
    print 'Turned on'
    
if not turned_on:
    print 'Turned off'


# ### 2.3 Ternary Operators
# 
# Traditionally if/else statements require multiple lines of code. Python has a very neat feature in which you can have an if/else in a single line! The syntax is quite simple:

# In[ ]:


fruit = 'Pear'
print 'Yes' if fruit == 'Apple' else 'No'


# ## 3. Loops

# ### 3.1 For Loops
# 
# Loops in Python use the same colon and indent notation as conditional statements.
# 
# Python uses `for x in iteratable` syntax, essentially a for each.

# In[ ]:


# Loops 10 times
for i in range(0, 10):
    print i


# **Lists**
# 
# We can easily iterate over a list. Traditionally in languages like Java we would do the following:

# In[ ]:


x = ['green', 'eggs', 'and', 'ham']
for i in range(0, len(x)):
    print x[i]


# But there is an easier way to do this in Python:

# In[ ]:


x = ['green', 'eggs', 'and', 'ham']
for element in x:
    print element


# **Dictionaries**
# 
# Iterating over dictionary elements is also quite easy and there are a couple of options. The first is as follows:
# 
# Note that the order is alphabetical based on keys.

# In[ ]:


shopping_list = {
    'milk': 1.2,
    'eggs': 0.99,
    'bread': 1.39
}
for item in shopping_list:
    cost_string = '{:.2f}'.format(shopping_list[item])
    print 'The item "%s" costs £%s.'% (item, cost_string)


# The second option uses the `iteritems` function which gives us direct access to both the key and the value of the given item from the dictionary.

# In[ ]:


shopping_list = {
    'milk': 1.2,
    'eggs': 0.99,
    'bread': 1.39
}
for item, price in shopping_list.iteritems():
    cost_string = '{:.2f}'.format(price)
    print 'The item "%s" costs £%s.'% (item, cost_string)


# ### 3.2 While Loops
# 
# While loops will be familiar syntax...

# In[ ]:


i = 0
while i < 10:
    print i
    i += 1


# ### 3.3 Other Iterables
# 
# In Python it is possible to iterate over other types such as strings:

# In[ ]:


s = "Hello, world!"
for character in s:
    print character


# ### 3.4 List Comprehensions
# 
# Similar to single-line conditional statements in Python, we can run a for loop in a single line. This can be used in the context of lists, as follows:

# In[ ]:


numbers = [1, 1, 2, 3, 5, 8, 13]
print [number * 2 for number in numbers] # Prints a the numbers list with each number doubled


# ## 4. Functions

# Functions (also known as methods in other languages) allow us to write a piece of reusable code, reducing duplication and making code easier to read and test.
# 
# ### 4.1 Declaring Functions
# In Python, functions are declared with the word `def`, followed by the function name, parentheses including parameter names (optional), followed by a colon. The same indentation rules apply as with loops and conditionals.

# In[ ]:


def say_hello():
    print 'hello'


# Functions are executed the same way as they would in Java:

# In[ ]:


say_hello()


# ### 4.2 Parameters
# 
# As with declaring variables in Python, we don't need to specify the types of parameters in Python. It would make sense to perform validation before executing code on variables passed in, but it is not imperative.

# In[ ]:


def add(a, b):
    result = a + b
    return result


print add(5, 6)


# Just to show you another example of parameters, this time a list printing function.

# In[ ]:


def print_list(their_list):
    for item in their_list:
        print item


print_list(['dog', 'cat', 'bird', 'mouse'])


# ### 4.3 Default Parameters
# 
# Python has the concept of "default parameters". When you write a function, you are able to set a default value for one of the parameters. When the function is called without the parameter specified, the default value will be taken for the execution of the function. To change the value when calling the function, you must specify the name of the parameter and the value you are assigning to it.

# In[ ]:


def say_hello(loud=False):
    if loud:
        print 'HELLO'
    else:
        print 'hello'
    return


say_hello()
say_hello(loud=True)


# ### 4.4 Recursion
# 
# If you haven't yet come across the concept of recursion, it is essentially when a function references itself, such as in this search algorithm below.
# 
# Be warned, recursion can quite easily result in an infinite loop!

# In[ ]:


def find_int(the_list, int_to_find):
    if the_list[0] == int_to_find:
        return 0
    return 1 + find_int(the_list[1:], int_to_find)


# In[ ]:


print find_int([1, 2, 3, 4, 5], 4)


# ### 4.5 Tuples
# 
# Tuples are groups of two or more values. They are unlike lists in that they provide a structure, while lists provide order. For example:

# In[ ]:


val1, val2 = (1, 2)
print val1
print val2


# In[ ]:


val3 = (2, 3)
print val3[0]


# This allows us to create functions that return multiple values at once.

# In[ ]:


def multiply_and_add(a, b):
    multiply = a * b
    add = a + b
    return multiply, add

mult, add = multiply_and_add(25, 35)
print mult
print add


# ## 5. Libraries

# Python has a lot of built-in functions, but many are not always available to developers until they are imported from their respective modules.
# 
# A full list of built-in Python modules can be found here: https://docs.python.org/2/py-modindex.html
# 
# ### 5.1 Importing Modules
# 
# The syntax for importing modules is: `import <module name>`
# 
# For example, `datetime` allows us to work with dates and times:

# In[ ]:


import datetime
print datetime.date.today()


# We can also import specific parts of a Python module with the `from` syntax:

# In[ ]:


from os import getcwd
print getcwd() # Prints the current working directory


# Modules can also be renamed:

# In[ ]:


from os import popen as run_command
print run_command('ls').read()


# ### 5.2 Local/Custom Modules
# 
# In many applications we write, we want to split our code up into different files. But how do you get access to code in another file?
# 
# Python is very consistent and lets us import all or part of another Python file. `aicamp.py` is located in the same directory as this notebook. Here's how easy it is to import it and execute a function in it:

# In[ ]:


import aicamp
aicamp.print_date()


# ** Importing from Another Directory **
# 
# To import a module from another directory, it gets a little bit more complicated. Here we are going to import `another_module.py` from a directory level with the parent directory.
# 
# `ai-camp-material/
#     Excercises/
#         0/
#             Python 101.ipynb
#             aicamp.py
#         custom_module_example/
#             another_module.py
#         ...`

# In[ ]:


import sys
sys.path.append('../custom_module_example')
import another_module
another_module.say_hello()


# ### 5.3 External Dependencies
# 
# There are a plethora of Python modules developed by third parties. The largest repository of these can be found on Pypi (https://pypi.python.org/pypi).
# 
# ** Pip **
# 
# Python uses `Pip` as its dependency manager. It's very easy to install modules using Pip. If you wanted to install a module named `requests` (a module used for HTTP requests), in the command line we would type:
# 
# `pip install requests`
# 
# This would give us access to the requests module from Python, using `import requests`.
# 
# You can also install a list of requirements from a text file using `pip install -r requirements.txt`.
# 
# ** Anaconda **
# 
# Anaconda is an alternative package manager that focuses mainly on data science modules. You can read more about it here: https://www.continuum.io/anaconda-overview
# 
# ** Virtual Environments **
# 
# When working with different projects, you might want to use different versions of certain modules. Virtual environments allow you to isolate dependencies on a project-by-project basis. You can read more about them here: http://docs.python-guide.org/en/latest/dev/virtualenvs/

# # 6. Miscellaneous
# 
# There are so many possibilities with Python and you should now be equipped to explore more of its capabilities on your own.
# 
# Here are a few more miscellaneous things that you may find useful.
# 
# ### 6.1 Exceptions
# 
# Exceptions occur at runtime when the Python interpreter can't run a piece of code for some reason. It isn't always a bad thing, exceptions should be expected and there are ways to easily handle them.
# 
# To prevent your program crashing, use a `try:` and `except:` block such as this:

# In[ ]:


exception_test = [1, 2, 3]
try:
    my_val = exception_test[4]
except:
    print 'There was an error'


# Quite often we want to be more specific than this generic error. We can actually access details about the error as below:

# In[ ]:


exception_test = [1, 2, 3]
try:
    my_val = exception_test[4]
except Exception, e:
    print 'Error details:'
    print type(e)
    print e


# Here we are using a generic `Exception` type, which will catch all exceptions. This isn't recommended as there may be different exceptions in different scenarios, which will require different ways to handle the situation.
# 
# You can see all the types of exceptions here: https://docs.python.org/2/library/exceptions.html

# In[ ]:


exception_test = [1, 2, 3]
try:
    my_val = exception_test[4]
except IndexError:
    print 'Handling index error'
except IOError:
    print 'Handling IO error'
except Error:
    print 'Handling all other errors'


# It's also possiblle in Python to execute code only if there were no exceptions using an `else:` statement:

# In[ ]:


try:
    print 'Testing'
except:
    print 'There was an error'
else:
    print 'There was no error'
print 'This will execute either way'


# **Debugging**
# 
# If you ever need to use a debugger in a Python notebook, it is a little bit awkward, but `Pdb` is the way to go.
# 
# `debug.set_trace()` will allow you to create a breakpoint in your code.

# In[ ]:


from IPython.core.debugger import Pdb
debug = Pdb()
def add(var1, var2):
    debug.set_trace() # Create a breakpoint
    result = var1 + var2
    return result


# Run the `add` function, and a console will allow you to interact with the variables at run time. Try running it and typing in one of the variable names.
# 
# `h` will give you a list of commands, while `c` will kill it.

# In[ ]:


add(1, 2)


# Just to show the code that would need to be added to a vanilla Python function to add debugging. The added lines are commented out below.

# In[ ]:


#from IPython.core.debugger import Pdb
#debug = Pdb()
def add(var1, var2):
#    debug.set_trace() # Create a breakpoint
    result = var1 + var2
    return result


# ### 6.2 Reading and Writing Files
# 
# ** Writing**
# 
# We use the `open` function in Python to open files. Below we open `test.txt` in the `w` mode, which stands for "write". This will allow you to write to the file, and create it if it doesn't already exist.
# 
# Don't forget to `close` the file once finished with it.

# In[ ]:


new_file = open('test.txt', 'w')
new_file.write('Hello, world!')
new_file.close()


# ** Reading **
# 
# For reading we also use `open`, but this time we specify the `r` mode, which stands for "read". We can now read the contents of the file.

# In[ ]:


input_file = open('test.txt', 'r')
print input_file.read()
input_file.close()


# ** CSV Files **
# 
# It's likely that you'll need to read a CSV file and get access to the data within it. We are going to use the Pandas module to import and read data from `data.csv`, a CSV file downloaded from the Open Data NI portal (https://www.opendatani.gov.uk/dataset/nihpi-by-propertytype).

# In[ ]:


import pandas
data = pandas.read_csv('data.csv')
data.head()             # Displays first five rows from data
data['Quarter Year']    # Displays all data from the 'Quarter Year' column
data['Quarter Year'][0] # Displays first row from the 'Quarter Year' column
data.describe()         # Displays a summary of numeric data


# We can easily create new rows based on other rows using the `apply` function, passing in another function which is executed on each value.

# In[ ]:


def double(row):
    return row * 2

data['Residential x2'] = data['NI Residential Property Price Index'].apply(double)

data


# ### 6.3 Data Visualisation
# 
# When it comes to machine learning, we're going to be doing quite a lot of visualisation of data, to help us get a better understanding of what's going on. Matplotlib is a graphing library that we will use to plot graphs from data.
# 
# Below is a simple example of plotting `[2, 4, 5, 8]` (y-axis) against `[1, 2, 3, 4]` (x-axis).

# In[ ]:


# For notebooks, we have to include this line to allow graphs to display in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [2, 4, 5, 8])
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.show()


# Let's try this out on something more meaningful. Using the CSV file from before, we want to try and see how the values have changed over time.
# 
# The problem is, our time column (Quarter Year) isn't numeric. We need to clean this up so that it's something like `2005.25` rather than `Q2 2005`. We can use the `apply` function to do this.
# 
# Note that this is an example of Feature Engineering!

# In[ ]:


import pandas
data = pandas.read_csv('data.csv')

def clean_year(row):
    components = row.split(' ') # e.g. splits 'Q1 2005' into ['Q1', '2005']
    year = int(components[1]) # Converts year from a string to an int
    quarter = int(components[0][1]) # Removes the 'Q' from the quarter (e.g. Q1 -> 1)
    decimal_quarter = (quarter - 1) * 0.25 # Q1 -> 0.0, Q2 -> 0.25 etc
    return str(year + decimal_quarter)

data['clean_year'] = data['Quarter Year'].apply(clean_year)


# Now we can nicely plot the Price Index against time.

# In[ ]:


plt.plot(data['clean_year'], data['NI Residential Property Price Index'])
plt.ylabel('NI Residential Property Price Index')
plt.xlabel('Year')
plt.show()


# It's also possible to plot multiple lines on a single graph, and provide a legend as below:

# In[ ]:


plt.plot(data['clean_year'], data['NI Detached Property Price Index'])
plt.plot(data['clean_year'], data['NI SemiDetached Property Price Index'])
plt.plot(data['clean_year'], data['NI Terrace Property Price Index'])
plt.plot(data['clean_year'], data['NI Apartment Price Index'])
plt.plot(data['clean_year'], data['NI Residential Property Price Index'])

plt.legend([
        'Detached',
        'SemiDetached',
        'Terrace',
        'Apartment',
        'Residential'
    ])
plt.xlabel('Year')

plt.show()


# ### 6.4 HTTP Requests

# Being able to perform HTTP requests is really handy, especially if you are integrating with an API.
# 
# If you want to learn more about HTTP requests in general, read up about them here: https://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177
# 
# ** GET **
# 
# The `requests` library makes it very easy to perform the likes of GET requests:

# In[ ]:


import requests

r = requests.get('https://www.google.com/')
print r.status_code


# ** POST **
# 
# Similarly, it allows you to POST data to a server. http://httpbin.org provides endpoints to test requests on.

# In[ ]:


data = {
    'name': 'Jo',
    'camp': 'A.I.Camp'
}
r = requests.post('http://httpbin.org/post', data)
print r.json()


# ** API **
# 
# The below might be even more useful. This is how easy it is to request data from an API, ready for manipulation!

# In[ ]:


import json

r = requests.get('https://www.opendatani.gov.uk/api/action/datastore_search?resource_id=b47a047d-5ed1-41ea-af13-2954b4a2bd92')
data = r.json() # Get the JSON data that was returned by the API
records_json = json.dumps(data['result']['records']) ## Get the data we are interested in, and get it into a nice format

pandas.read_json(records_json) # 


# ### 6.5 Numpy
# 
# We'll be using Numpy from time to time in A.I.Camp. It's basically a library that gives you powerful access over multi-dimensional arrays. This will be particularly useful for vision processing when we want to represent and image in numerical form.
# 
# There's not a lot to it, but you can read more about it here: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
# 
# Below we create a Numpy array of numbers from 1 to 10.

# In[ ]:


import numpy as np

numpy_test = np.arange(1, 11)
print numpy_test


# Numpy has several built-in manipulation functions, including `reshape(x,y)`, where `x` is the number of rows and `y` is the number of columns. The product of x and y must equal the product of the rows and columns of the orginal array.

# In[ ]:


numpy_test.reshape(2,5)


# We can also specify the step size as a third parameter in `arange`.

# In[ ]:


numpy_test = np.arange(0, 10, 0.5)
print numpy_test


# In[ ]:




