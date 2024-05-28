import time

print("\n\nPlanetary distances at your fingertips. No spaceship required.\n") #Welcome message
time.sleep(2)



planet_sun_distance = {
    "mercury": 58000000,
    "venus": 108000000,
    "earth": 150000000,
    "mars": 228000000,
    "jupiter": 778000000,
    "saturn": 1400000000,
    "uranus": 2900000000,
    "neptune": 4500000000,
}

# User input, first planet
planet1_input = input("Enter name of first planet: ")
planet1 = planet1_input.lower()
time.sleep(2)

planet2_input = input("\nEnter the name of your second planet: ")
planet2 = planet2_input.lower()

# if planet1 == "mercury":
#     print("\nDid you know, Mercury is 58 million km from the sun.")
# elif planet1 == "venus":
#     print("\nDid you know, Venus is 108 million km from the sun.")
# elif planet1 == "earth":
#     print("\nDid you know, Earth is 150 million km from the sun.")
# elif planet1 == "mars":
#     print("\nDid you know, Mars is 228 million km from the sun.")
# elif planet1 == "jupiter":
#     print("\nDid you know, Jupiter is 778 million km from the sun.")
# elif planet1 == "saturn":
#     print("\nDid you know, Saturn is 1.4 billion km from the sun.")
# elif planet1 == "uranus":
#     print("\nDid you know, Uranus is 2.9 billion km from the sun.")
# elif planet1 == "neptune":
#     print("\nDid you know, Neptune is 4.5 billion km from the sun.")
# elif planet1 == "":
#     print("\nOops...you need to enter a name to continue")
#     exit()
# else:
#     print("\nOops...that planet might not be in this Galaxy. Try again.")
#     exit()
# time.sleep(1)




# calculations
distance_km = abs()

first_planet = planet1_input.title()
second_planet = planet2_input.title()

template = f"\nThe distance between {first_planet} and {second_planet} is {distance_km} km."

print(template)





    



