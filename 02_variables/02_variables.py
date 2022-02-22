calculation_to_sec = 24 * 60 * 60
calculation_to_hours = 24
name_of_unit = 'seconds'

print(f"20 days are { 20 * calculation_to_sec } seconds")
print(f"20 days are { 35 * calculation_to_sec } {name_of_unit}")
print(f"20 days are { 35 * calculation_to_hours } hours")

def power(num, x=1):
    result = 1
    print(x)
    for i in range(x):
        result = result * num
    return result

print(f'The power of 2 is',power(2))
print(f'The power of 3,3 is ',power(3,3))