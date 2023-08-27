example_list = ["element A", "element B", "element C"]

print("#simple print")
print(example_list)
print()

print("#enumerate() function print")
print(enumerate(example_list))
print()

print("coercion output with list() function")
print(list(enumerate(example_list)))
print()

print("combining with for loop")
for i, value in enumerate(example_list):
    print("{} element is {}.".format(i, value))
    