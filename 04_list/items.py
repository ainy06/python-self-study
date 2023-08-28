example_dictionary = {
    "key A": "value A",
    "key B": "value B",
    "key C": "value C",
}

print("#dictionary's items() function")
print("items():", example_dictionary.items())
print()

print("dictionary's items() function and loop combined")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))