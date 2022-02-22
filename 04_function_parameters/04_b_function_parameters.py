#Global scope: variables available from within any scope
calculation_to_minutes = 24 * 60
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are { num_of_days * 60} {name_of_unit}"

#calling the functions
my_var = days_to_units(50)
print(my_var)