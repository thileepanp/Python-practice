# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:37:01 2018

@author: thileepan

Studying how to create a class: 


Refer to basics of class in the 'example_class.py' code. 

So, we know that when a class instance is created, it 
inherits all the attributes(variables) and methods(functions)
of the class. But what if we need to add new attributes and 
functions to the class. This is where we can use inheritance again. 

Python makes inheritance really easily. We define a new class, 
based on another, 'parent' class. Our new class brings everything 
over from the parent, and we can also add other things to it. If any 
new attributes or methods have the same name as an attribute or method 
in our parent class, it is used instead of the parent one. 


"""

# An example to demonstrate inheritance. 

from example_class import Shape

class square(Shape):
	"""docstring for square"""
	def __init__(self, x):
		self.x = x
		self.y = x



""" 
To invoke this class run the command 'run classinheritance.py'. 
Then create an  instance of this class by calling the classname with
the attribute and assigning an instancename to it for example 
'instance_name = square(5)'. 

Now, all the methods created in example_class.py will be inherited 
by this new instance. 

To make calculations, we can invoke the instance_name.method() command. 
example instance_name.area(), instance_name.perimeter()

"""


""" It is just like normally defining a class, but this time we 
put in brackets after the name, the parent class that we inherited 
from. As you see, we described a square really quickly because 
of this. That's because we inherited everything from the shape
class, and changed only what needed to be changed. In this case 
we redefined the __init__ function of Shape so that the X and Y 
values are the same."""
		