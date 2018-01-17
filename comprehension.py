""" 
SET, LIST AND DICTIONARY COMPREHENSION

The common structure for comprehension with sets, lists or dictionarys is 

"""

#LIST COMPREHENSION 

list_comprehension = [expression for value in collection if condition] #List comprehension format

x_list = [1,23,4,567, 98]
list_compr = [x**2 for x in x_list if x>1]


# SET COMREHENSION

set_comprehension = {expression for value in collection if condition} #set comprehension format

X_set = {1,23,4,567,98}
set_compr = {str(x) for x in X_set if x>1}


# DICTIONARY COMPREHENSION

dict_comprehension = {key_expression : value_expression for value in collection if condition #format
x_dict = {'One':1, 'Two':2, 'Twenty three':23, 'Four':4, 'Ninety Eight':98}
dict_compr = {type(key):type(value) for key,value in enumerate(x_dict) if value[0]=='O'}



# NESTED LIST COMPREHENSION
x_dict = {'One':1, 'Two':2, 'Twenty three':23, 'Four':4, 'Ninety Eight':98}
y_dict = {0:'first', 1:'second', 2:'third',3:'fourth',4:'fifth'}

dict_list = [x_dict,y_dict]

result_list= [key for dictionary in dict_list for key in dictionary if type(key) == str]

#If we use loops this comprehension could be written as

result_list = []

for dictionary in dict_list:
	for key in dictionary:
		if type(key) == str:
			result_list.append(key)
return result_list


