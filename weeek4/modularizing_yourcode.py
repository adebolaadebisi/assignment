# modularizing your code2
#3. Python modules
# what a module is (a.py file that can be reused)
# importing built-in modules(math,random,datetime)
# writing your own module(creating my_module.py and importing it)
# aliasing modules(import numpy as np)

#what is a module?
# a module in python is simply a file with.py extension that contains python code(functions,variables, or classes)which can be reused in other programs.
# instead of writing the same code again and again, you can write it once in a module and then import it anywhere.
# lets think of a module as a toolbox. each tool (function, variable, or class) can be taken out and used whenever needed, without rebuilding the tool from scratch.

# importing built-in modules
# python already comes with many pre-built modules that you can use directly.
# some common examples are:
#math-for mathematical operations
# random- for generating random numbers
# datetime - for working with dates and time.
#etc.
# to use built in modules,you have to load them into your environment, that is, import them.
# Different ways to import modules
#1. Import the whole module
import math
# lets put it to use
print(math.sqrt(9))
#- Note that you must specify the module name when calling a function within it.
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[4], line 8
#       3 import math
#       6 # Lets put it to use
# ----> 8 print(math.sqrt())
#       9 # - Note that you must specify the module name when calling a function within it.

#ypeError: math.sqrt() takes exactly one argument (0 given)
#1. import as an alias
import math as m
#lets put it to use
print(m.sqrt(25))
#- this shorten the module name, this is common with libraries like numpy, pandas, etc

#2. import specific functions or variables
from math import sqrt, pi
print(sqrt(36))
print(pi)
#- here you dont need the prefix 'math'. anymore
#3. import everything from the module
from math import *
print(sqrt(49))
print(pi)
#- This is usually not recommended because it can cause name conflicts if two modules have function with the same name