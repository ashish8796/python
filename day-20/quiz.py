def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as cast:
        for line in cast:
            i = line.find(",")
            name = line[:i]
            cast_list.append(name)
    
    return cast_list
cast_list = create_cast_list("flying_circus_cast.txt")
for actor in cast_list:
    print(actor)

#OR
def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as f:
        for line in f:def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as cast:
        for line in cast:
            i = line.find(",")
            name = line[:i]
            cast_list.append(name)
    
    return cast_list
cast_list = create_cast_list("flying_circus_cast.txt")
for actor in cast_list:
    print(actor)

#OR
def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)
    return cast_list
cast_list = create_cast_list("flying_circus_cast.txt")
for actor in cast_list:
    print(actor)

            name = line.split(",")[0]
            cast_list.append(name)
    return cast_list
cast_list = create_cast_list("flying_circus_cast.txt")
for actor in cast_list:
    print(actor)
