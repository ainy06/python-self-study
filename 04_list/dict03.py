# declare dictionary 
dictionary = {
    "name": "7D Dried Mango",
    "type": "snack"
}

# print before element delete
print("before delete elements", dictionary)

# delete elements in dictionary 
del dictionary["name"]
del dictionary["type"]

# print after delete 
print("after delete elements", dictionary)
