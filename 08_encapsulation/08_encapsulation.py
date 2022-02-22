#Encapsulation: the process of wrapping up variables and methods into a single entity/ scope
calculation_to_minutes = 24 * 60
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(type(num_of_days))
    if(num_of_days > 0):
        return f"{num_of_days} days are { num_of_days * 24} {name_of_unit}"
    elif(num_of_days == 0):
        return "You entered zero, please enter a positive value!"
    else:
        return "You entered invalid format!"

def validate_and_execute():
    if user_input.isdigit():
        my_var = days_to_units(int(user_input))
        print(my_var)
    else:
        print("Your input is not a valid number, please don't ruin my program")

#calling the functions
user_input = input("Please enter number of days:")
validate_and_execute()

