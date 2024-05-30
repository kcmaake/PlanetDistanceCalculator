import time

print("\n\nPlanetary distances at your fingertips. No spaceship required.\n") #Welcome message
time.sleep(2)


planets = [
    {
       "name": "mercury",
       "distance": 58000000,
       "fun_fact": "Did you know, Mercury is 58 million km from the sun."
    },
    {
      "name": "venus",
      "distance": 108000000,
      "fun_fact": "Did you know, Venus is 108 million km from the sun." 
    },
    {
      "name": "earth",
      "distance": 150000000,
      "fun_fact": "Did you know, Earth is 150 million km from the sun."
    },
    {
      "name": "mars",
      "distance": 228000000,
      "fun_fact": "Did you know, Mars is 228 million km from the sun."
    },
    {
      "name": "jupiter",
      "distance": 778000000,
      "fun_fact": "Did you know, Jupiter is 778 million km from the sun."
    },
    {
      "name": "saturn",
      "distance": 1400000000,
      "fun_fact": "Did you know, Saturn is 1.4 billion km from the sun."
    },
    {
      "name": "uranus",
      "distance": 2900000000,
      "fun_fact": "Did you know, Uranus is 2.9 billion km from the sun."
    },
    {
      "name": "neptune",
      "distance": 4500000000,
      "fun_fact": "Did you know, Neptune is 4.5 billion km from the sun."
    }
]


# Function checks user input, finds planet nd returns it's distance
def get_planet_distance(planets):
  if user_input == 'quit':
    return None  

  for planet in planets:
    if user_input == planet["name"].lower():
      planet_distance = planet["distance"]  
      break 

  if planet_distance is not None:  
    return planet_distance  
  else:
    print(f"Planet '{user_input}' not found. Please try again.")

# User inputs
user_input = input("Enter the name of a planet (or 'quit' to exit): ").lower()
user_input1 = user_input.capitalize()
planet_distance1 = get_planet_distance(planets)

user_input = input("Enter the name of a planet (or 'quit' to exit): ").lower()
user_input2 = user_input.capitalize()
planet_distance2 = get_planet_distance(planets)
 

# Calculations
result = abs(planet_distance1 - planet_distance2)
print(f'{user_input1} and {user_input2} are {result} km apart')


      









    



