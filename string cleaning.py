""" 
Functions to clean strings!!

"""

import re


def remove_punctuation(value):
	return re.sub('[!@#$%^&*()"''<>?/,.~`{}[]\|]', '', value)


clean_ops = [str.strip, remove_punctuation,str.title]

result =[]
def clean_strings(strings, ops):
	for value in strings:
		for function in ops:
			value = function(value)
		result.append(value)
	return(result)



#To run the operation run

clean_strings(string_list, clean_ops)