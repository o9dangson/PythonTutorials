##############################
# PYTHON CHEATSHEET 
##############################
# Basic Print Statement                             #   This is a comment. This will allow one line of characters to be used as descriptions of nearby code.
                                                    #   Comments are useful for keeping organized, clean code.
print("Hello World! This is the first commit!")     #   This is a print statement. It prints to the screen the string inside quotation marks.

# Python Keywords (Must be type as they are seen)
""" List of Keywords
    False       await   else    import  pass        None    
    break       except  in      raise   True        class
    finally     is      return  and     continue    for
    lambda      try     as      def     from        nonlocal
    while       assert  del     global  not         with
    async       elif    if      or      yield
"""
# Python Identifier
variable = 1                                        #   Identifiers can be any length, but cannot hold special characters and can't start with a number
x3 = 2                                              #   Python is case sensitive
my_Var_Y = 'This identifier is valid'               #   Underscore, '_', can be used in identifiers
myList = [1,2,3]
# 3Var is not valid
print("variable = %d; x3 = %d; my_Var_Y = %s; myList = %s" % (variable, x3, my_Var_Y, myList))   # %d refers to numbers, %s refers to strings or lists

# Python Statement, Indentation, and comments
a = 1 + 2 + \
    3                                               # Multilined statement
b = (1 + 2 + 
    3)                                              # Same thing. Can also be done with [] or {}
c = b; d = c; e = a                                 # Multiple statements in a line.
def double(num):
    """Function that returns double the value of the input 'num'"""     # This is a function definition that is return when print(double.__doc__) is run
    return 2*num
print(double.__doc__)

# Variables
a, b, c = 10, 20.3, "hello"                         #   You can assign multiple things on the same line.
print("a = %d; b = %d; c = %s" % (a, b, c))
a = b = c = "same"                                  #   Or multiple things to the same thing
print("a = %s; b = %s; c = %s" % (a, b, c))

# Constants
import constant                                     # Constants are usually created and assigned in a module. Here the module is an individual file
print(constant.PI)
print(constant.GRAVITY)

# Literals
a = 0b1010      # Binary Literal:   10
b = 100         # Decimal Literal:  100
c = 0o310       # Octal Literal:    200
d = 0x12c       # Hexadecimal Literal: 300
float_1 = 10.5  # Float Literals
float_2 = 1.5e2
x = 3.14j       # Complex Literal
print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

strings = "This is a string"
char    = "C"
multiline_str   =   """This is a
multiline string."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"\tRaw\nString"
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

x = (1 == True) # Boolean literal
print("x is", x)

food = None # Special Literal used to specify that the field has not been assigned
print(food)

# Literal Collections
fruits = ["apple", "mango", "orange"]               #list
numbers = (1, 2, 3)                                 #tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'} #dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}                  #set
print(fruits)
print(numbers)
print(alphabets)
print(vowels)

# Python Datatypes
a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number:", isinstance(a, complex))