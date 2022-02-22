calculation_to_minutes = 24 * 60
name_of_unit = "house"

#word def use to define the function
""" def days_to_units(num_of_days):
    print(f"{num_of_days} days are { num_of_days * 60} {name_of_unit}") """

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are { num_of_days * 60} {name_of_unit}")
    print(custom_message)

#calling the functions
""" days_to_units(20) 
days_to_units(30)
days_to_units(40) """
days_to_units(50, "Hello")