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