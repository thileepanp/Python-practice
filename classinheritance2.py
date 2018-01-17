# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:37:01 2018

@author: thileepan

Studying how to create a class: 

To know how to create class and inheritance check the codes
example_class.py and classinheritance.py. 

Let's take from what we have learnt, and create another 
new class, this time inherited from Square. Remember, the 
Square class is already inherited from Shape class and has 
inherited all the methods and variables from that class. It will be two
squares, one immediately left of the other:

The shape looks like this:
 _________
|    |    |
|    |    |
|____|____|

"""
from classinheritance import square # importing the already existing class

class doublerectangle(square): #creating the class
	"""docstring for doublerectangle"""
	def __init__(self, y): # defining the class attributes
		self.x = 2 * y     # assigning the input variable given while creating the instance to the class attributes
		self.y = y

# creating a new method inside this class, since this class is inherited from the 
# another class, the method 'perimeter' is also inherited. But since we need to 
# create a new method for perimeter, we are creating a new method here, so in all 
# the instances created using this class, the new method and variable will only be used.  
	def perimeter(self):   
		return 2*self.x + 3*self.y


# in order to create an instance of this class and perform operations, 
#first run the class in ipython as 'run classinheritance2.py'. Then create an 
#instance of this class by calling the classname with the attribute and assigning an 
#instancename to it example 'instance_name = doublerectangle(5)'
#now, all the methods created in example_class.py will be inherited by this new instance and 
#but the 'perimeter' method will be as per the new method created here. 

# To make calculations, we can invoke the instance_name.method() command. 
#example instance_name.area(), instance_name.perimeter()







