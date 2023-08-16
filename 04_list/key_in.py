# declare dictionary
dictionary = {
    "name": "7D Dried Mango",
    "type": "snack",
    "ingredient": ["Mango", "Sugar", "Sodiumetabisulfite", "Yellowpigment"],
    "origin": "Philippine"
}

# get input from user
key = input("> key to access: ")

# print
if key in dictionary:
    print(dictionary[key])
else:
    print("You are accessing a key that does not exist.")
