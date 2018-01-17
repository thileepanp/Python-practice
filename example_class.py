# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:37:01 2018

@author: thileepan

Studying how to create a class

A class is an object, it is a datastructure that holds the values
and also the methods to process the data. Likewise, variables, 
functions, lists and dictionaries are also classes. 

1. A variable inside a class is called an attribute 
2. A function inside a class is called a method. 

Therefore a class holds together attribute(variables) and methods(
functions) so that both the data and the code to process it is in
the same spot. 

We can create any number of instances of that class so that we don't
have to write new code for every new object(instance) we create. 

"""

# An example to demostrate how to create a classs 

class Shape: #defining the name of the class

    """ Self is how we refer to things in the class from the class itself
    Self is the first parameter in any function defined inside a class.
    Any function or variable created on the first level of indendation
    (that is  lines of code that start one TAB to the right of where 
    we put class Shape is automatically put into self.) To access these
    functions or variables else where inside the class, their names must
    be preceeded with self and full-stop e.g. self.x """
    def __init__(self,x,y): 
        self.x = x
        self.y = y
    description = "this shape has not been described"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
    	return self.x *self.y
    def perimeter(self):
    	return 2*self.x + 2*self.y
    def describe(self, text):
    	self.description = text
    def authorName(self, text):
    	self.author = text
    def scaleSize(self,scale):
    	self.x = self.x * scale
    	self.y = self.y * scale



""" 
To invoke this class, run the command as 'run example_class.py'

Then create an  instance of this class by calling the classname with
the attribute and assigning an instancename to it for example 
'instance_name = Shape(5)'

Now, all the methods will be inherited by this new instance. 

To make calculations, we can invoke the instance_name.method() command. 
example instance_name.area(), instance_name.perimeter()

"""


""" In order to use this class first run the class using 'run example_class'.
Then we can create a new instance of the class using the class name and 
passing the variables needed to it. We can also assign a name to the instance 
of that class. E.g. 'rectangle = Shape(100,45)'. Here we create
an instance of the class and named it as rectangle. 

The __init__ function really comes into play at this time. We create an instance 
of a class by first giving its name (in this case, Shape) and then, in brackets, 
the values to pass to the __init__ function. The init function runs (using the
parameters you gave it in brackets) and then spits out an instance of that class,
 which in this case is assigned to the name rectangle.

Now that the instance of that class named rectangle belongs to the class Shape,
it inherits all the properties of the class, that means, all the functions and 
the variables in the class 'Shape' becomes a part of the new class instance called
rectangle.

Just like how we used 'self' inside the class to refer to the variables and the functions
of the class, we can now use the instance name 'rectangle' to refer to the 
variables and the functions that instance inheritted from main class. 

therfore, If I want to find the area of the rectangle, I can use the instance 
name along with the inheritted function like rectangle.area(), rectangle.perimeter() etc., 



"""