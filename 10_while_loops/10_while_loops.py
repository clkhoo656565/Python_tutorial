#Encapsulation: the process of wrapping up variables and methods into a single entity/ scope
calculation_to_minutes = 24 * 60
name_of_unit = "hours"

def days_to_units(num_of_days):
    return num_of_days * 24
    

def validate_and_execute():
    try:
        
        converted_value = int(user_input)
        if(converted_value > 0):
            result = days_to_units(converted_value)
            print(f"{converted_value} days are {result} {name_of_unit}")
        elif(converted_value == 0):
            print("You entered zero, please enter a positive value!")
        else:
            print("You entered invalid format!")
            
    except ValueError:
        print("Your input is not a valid number, please don't ruin my program")

#calling the functions
user_input = ""
while user_input != "exit":
    user_input = input("Please enter number of days:")
    validate_and_execute()

