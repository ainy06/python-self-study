# declare dictionary
dictionary = {
    "name": "7D dried mango",
    "type": "snack",
    "ingredient": ["mango", "sugar", "sodiumtabisulfite", "yellowpigment"],
    "origin": "Philippine"
}

# Attempt to access a key that does not exist. 
value = dictionary.get("key does not exist")
print("value:", value)

# check None
if value == None:
    print("You accessed a key that does not exist.")