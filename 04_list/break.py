i = 0

while True:
    print("repeat {} times.".format(i))
    i = i + 1
    input_text = input("> Are you sure you want to quit?(y/n): ")
    if input_text in ["y", "Y"]:
        print("end loop.")
        break