import time

print("\n\nPlanetary distances at your fingertips. No spaceship required.\n") #Welcome message
time.sleep(2)

# User input, first planet
planet1_input = input("Enter name of first planet: ")
planet1 = planet1_input.lower()
time.sleep(2)


if planet1 == "mercury":
    planet1_distance = 58000000
    print("\nDid you know, Mercury is 58 million km from the sun.")
elif planet1 == "venus":
    planet1_distance = 108000000
    print("\nDid you know, Venus is 108 million km from the sun.")
elif planet1 == "earth":
    planet1_distance = 150000000
    print("\nDid you know, Earth is 150 million km from the sun.")
elif planet1 == "mars":
    planet1_distance = 228000000
    print("\nDid you know, Mars is 228 million km from the sun.")
elif planet1 == "jupiter":
    planet1_distance = 778000000
    print("\nDid you know, Jupiter is 778 million km from the sun.")
elif planet1 == "saturn":
    planet1_distance = 1400000000
    print("\nDid you know, Saturn is 1.4 billion km from the sun.")
elif planet1 == "uranus":
    planet1_distance = 2900000000
    print("\nDid you know, Uranus is 2.9 billion km from the sun.")
elif planet1 == "neptune":
    planet1_distance = 4500000000
    print("\nDid you know, Neptune is 4.5 billion km from the sun.")
elif planet1 == "":
    print("\nOops...you need to enter a name to continue")
    exit()
else:
    print("\nOops...that planet might not be in this Galaxy. Try again.")
    exit()
time.sleep(1)


planet2_input = input("\nEnter the name of your second planet: ")
planet2 = planet2_input.lower()

if planet2 == "mercury":
    planet2_distance = 58000000
elif planet2 == "venus":
    planet2_distance = 108000000
elif planet2 == "earth":
    planet2_distance = 150000000
elif planet2 == "mars":
    planet2_distance = 228000000
elif planet2 == "jupiter":
    planet2_distance = 778000000
elif planet2 == "saturn":
    planet2_distance = 1400000000
elif planet2 == "uranus":
    planet2_distance = 2900000000
elif planet2 == "neptune":
    planet2_distance = 4500000000
elif planet2 == "":
    print("Oops...you need to enter a name to continue")
    exit()
else:
    print("Oops...that planet might not be in this Galaxy. Try again.")
    exit()
time.sleep(2)


# calculations
distance_km = abs(planet1_distance - planet2_distance)

first_planet = planet1_input.title()
second_planet = planet2_input.title()

template = f"\nThe distance between {first_planet} and {second_planet} is {distance_km} km."

print(template)





    



