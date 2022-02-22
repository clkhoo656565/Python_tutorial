#Modules use to logically organize your Python code and module should contain only related code
from helper import validate_and_execute, user_input_message # only import certain functions or variables from helper.py module

""" 
#Will import everything from helper.py module

from helper import *

OR

import helper

OR

import helper as h
 """

user_input = input(user_input_message)
days_and_unit = user_input.split(":")
print(days_and_unit)
days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]} #{"days": 20, "unit":"hours"}
print("Type of days_and_unit_dictionary: ", type(days_and_unit_dictionary))
print("days_and_unit_dictionary: ", days_and_unit_dictionary)
validate_and_execute(days_and_unit_dictionary)