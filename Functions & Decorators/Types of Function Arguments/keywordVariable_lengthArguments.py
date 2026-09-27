def build_profile(**details):
    print("----- Profile Card -----")

    for key, value in details.items():
        print(key.capitalize(), ":", value)


# First profile
build_profile(
    name="Navya",
    age=18,
    city="Vizianagaram",
    hobby="Coding"
)

print()

# Second profile
build_profile(
    name="Meera",
    age=19,
    city="Hyderabad",
    hobby="Reading"
)
#----- Profile Card -----
#Name : Navya
#Age : 18
#City : Vizianagaram
#Hobby : Coding

#----- Profile Card -----
#Name : Meera
#Age : 19
#City : Hyderabad
#Hobby : Reading
