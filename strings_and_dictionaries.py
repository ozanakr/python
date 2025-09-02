x = "hello"
y = 'hello'
print(x == y)

print('My dog is named "Pluto"')
print("1 \n 2 \n  3")

triplequoteexample = """hello
 ozan
bio
"""
print(triplequoteexample)

# by default, print func outs a n after the execution
print("hello", end='')
print("pluto", end='')

name = "Ozan"
#indexing
print(name[0])
#slicing
print(name[:2])
#lenght of the string
print(f"length of the name: {len(name)}")
#looping over the string
print([char + "! " for char in name])
#strings are immutable
print(name.upper())
print(name.lower())
#indexing in a long string sequence
claim = "My travel plan is ready"
claim.index("plan") # output is 11
print(claim.startswith("My"))
print(claim.endswith("ozan"))
#splitting each word from the sequence of a str
words = claim.split()
print(words)
datestr = '1956-01-31'
year, month, day = datestr.split('-')
date_tidy = "/".join([month, day, year])
print(date_tidy)
#putting unicode chars
print(" 👏 ".join([word.upper() for word in words]))
#building strings with format
print(name + ", likes to play nintendo games")
planet = "pluto"
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass / earth_mass, population,))
# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)
#dictionary comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[:3] for planet in planets}

print("\n".join([f"{a}: {b}" for a, b in planet_to_initial.items()]))

help(str)