#Global scope: variables available from within any scope
calculation_to_minutes = 24 * 60
name_of_unit = "hours"

#Local scope: variables created inside function can only be use inside that function
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are { num_of_days * 60} {name_of_unit}")
    print(custom_message)

def days_to_units(num_of_days):
    print(f"{num_of_days} days are { num_of_days * 60} {name_of_unit}")

""" 
#DO NOT DELETE, it is reference
def scope_check():
    print(name_of_unit)
    print(num_of_days) #num_of_days is not global variable and does not available in this scope 
"""

def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)


#calling the functions
scope_check(50)
days_to_units(50)