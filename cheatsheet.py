##############################
# PYTHON CHEATSHEET 
##############################
# Basic Print Statement                             #   This is a comment. This will allow one line of characters to be used as descriptions of nearby code.
                                                    #   Comments are useful for keeping organized, clean code.
print("Hello World! This is the first commit!")     #   This is a print statement. It prints to the screen the string inside quotation marks.

################################################################
# Python Keywords (Must be type as they are seen)
################################################################
""" List of Keywords
    False       await   else    import  pass        None    
    break       except  in      raise   True        class
    finally     is      return  and     continue    for
    lambda      try     as      def     from        nonlocal
    while       assert  del     global  not         with
    async       elif    if      or      yield
"""
################################################################
# Python Identifier
################################################################
variable = 1                                        #   Identifiers can be any length, but cannot hold special characters and can't start with a number
x3 = 2                                              #   Python is case sensitive
my_Var_Y = 'This identifier is valid'               #   Underscore, '_', can be used in identifiers
myList = [1,2,3]
# 3Var is not valid
print("variable = %d; x3 = %d; my_Var_Y = %s; myList = %s" % (variable, x3, my_Var_Y, myList))   # %d refers to numbers, %s refers to strings or lists

################################################################
# Python Statement, Indentation, and comments
################################################################
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

################################################################
# Literals
################################################################
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

################################################################
# Literal Collections
################################################################
fruits = ["apple", "mango", "orange"]               #list
numbers = (1, 2, 3)                                 #tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'} #dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}                  #set
print(fruits)
print(numbers)
print(alphabets)
print(vowels)

################################################################
# Python Datatypes
################################################################
a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number:", isinstance(a, complex))

#   [] Lists don't have to be the same type
#   () Tuples can't be modified
#   {} Sets are unordered collection of items
#   {:} Dictionaries are unordered collection of key-value pairs

#   Conversion btwn compatible types is possible 
#       ie. int(), float(), str(), set(), tuple(), list(), dict()

################################################################
# Python Conversion
################################################################
#   implicit conversion is done automaticlly without user involvement
#   explicit conversion is done by user
num_int = 123
num_str = "456"
print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str
print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:", type(num_sum))

################################################################
# Python Input, Output and Import
################################################################
#   Output Formatting
x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))
print('The value of x is {1} and y is {0}'.format(x,y))     # Order can be designated in {}
print('Hello {name}, {greeting}'.format(greeting = 'Good Morning!', name = 'John'))
                # Keyword arguments can also be used
print('The value of x is %3.2f' %x)         # Also can be done using old sprintf() in C
           
#   Input
#           input(prompt)   is the syntax. Note that the value stored is a string datatype
str_example = input(["Prompt for Input"])
print('str_example:', str_example)

################################################################
# Python Operators
################################################################
# Arithmetic Operators
#   + - * / 
#   % (modulus)   // (Floor division)     ** (Exponent)
# Comparator Operators
#   > < == != =! >= <=
# Logical Operators
#   and   or  not
# Bitwise Operators
''' &   (bitwise AND)
    |   (bitwise OR)
    ~   (bitwise NOT)
    ^   (bitwise XOR)
    >>  (bitwise right shift)
    <<  (bitwise left shift)
'''
# Assignment Operators (does calculation before assignment)
#           =   +=  -=  *=  /=  **= &=  |=  ^=  >>= <<=
#           eg. x+=5  is the same as x = x+5

# Special Operators (is, is not)
#    Identity Operators (used to check if two values/variables located in same memory)
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)         # False
print(x2 is y2)             # True
print(x3 is y3)             # False

#   Membership Operators (in, not in)
x = 'Hello World'
y = {1:'a', 2:'b'}

print('H' in x)         # True
print('hello' not in x) # True
print(1 in y)           # True
print('a' in y)         # False; a is a value not a key so it isn't found

################################################################
# Python Namespace and Scope
################################################################