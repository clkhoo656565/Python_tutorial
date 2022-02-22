#Encapsulation: the process of wrapping up variables and methods into a single entity/ scope
calculation_to_minutes = 24 * 60
name_of_unit = "hours"

def days_to_units(num_of_days):
    return num_of_days * 24

def calculate_minutes(hours):
    return hours * 60

def calculate_seconds(minutes):
    return minutes * 60
    

def validate_and_execute():
    try:
        
        converted_value = int(num_of_days_elements)
        if(converted_value > 0):
            hours = days_to_units(converted_value)
            total_minutes = calculate_minutes(hours)
            total_seconds = calculate_seconds(total_minutes)
            print(f"{converted_value} days are {hours} {name_of_unit} and {total_minutes} minutes and {total_seconds} seconds")
        elif(converted_value == 0):
            print("You entered zero, please enter a positive value!")
        else:
            print("You entered invalid format!")
            
    except ValueError:
        print("Your input is not a valid number, please don't ruin my program")

#calling the functions
user_input = ""
while user_input != "exit":
    user_input = input("Please enter number of days as a comma separated list:")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_elements in user_input.split(","): #split(",") to split the each elements after comma which entered by the user into list, for example 1, 2, 3
        validate_and_execute()

