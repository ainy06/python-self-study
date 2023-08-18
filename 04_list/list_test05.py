# declare dictionary 
character = {
    "name": "Berserker",
    "level": 60,
    "items": {
        "sword": "banana",
        "armor": "awesome suit"
    },
    "skill": ["rage", "strong rage" "extreme rage"]
}

# use for loop
for key in character:
    if type(character[key]) is dict:
        for inner_key in character[key]:
            print(inner_key, ":", character[key][inner_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":",  character[key])