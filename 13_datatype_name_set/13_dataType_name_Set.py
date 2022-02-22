months_list = ["January", "February", "March"]
print("Original month list: ", months_list)
months_list.append("April") #append only can take one argument
months_list.extend(["April", "May", "June"]) #extend can add additional multiple elements
print("Month_list after append and extend")
print(months_list)
print("Month_list after SET()")
print(set(months_list)) 
months_list.remove("April")
print("Month_list after remove 'APRIL '")
print(months_list)

