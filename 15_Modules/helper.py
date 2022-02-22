#Dictionary are used to store values in key: value pairs; Is a collection, which does not allow duplicate values
calculation_to_minutes = 24 * 60
name_of_unit = "hours"

def days_to_hours(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24 } hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60 } minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input = int(days_and_unit_dictionary["days"])
        if(user_input > 0):
            result = days_to_hours(int(days_and_unit_dictionary["days"]), days_and_unit_dictionary["unit"])
            print(result)
        elif(user_input == 0):
            print("You entered zero, please enter a positive value!")
        else:
            print("You entered invalid format!")
            
    except ValueError:
        print("Your input is not a valid number, please don't ruin my program")

user_input_message = "Please enter number of days and conversion unit:"