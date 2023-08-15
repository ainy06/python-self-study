# declare dictionary 
dictionary = {
    "name": "7D Dried Mango",
    "type": "snack",
    "ingredient": ["mango", "sugar", "sodiummetabisulfite", "yellowpigment"],
    "origin": "Philippine"
}

# print
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

# change value
dictionary["name"] = "8D Dried Mango"
print("name:", dictionary["name"])

# change new value 
dictionary["name"] = "8D Dried Pineapple"

# add price
dictionary["price"] = 5000
print("price:", dictionary["price"])
print()

# delete certain element
del dictionary["ingredient"]

