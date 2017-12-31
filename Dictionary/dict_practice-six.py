
# Practice of Dictionary Data-Structure

# Practice Example with loop and dictionary

world_largest_rivers = {
    'egypt': 'nile',
    'pakistan': 'sindh',
    'india': 'ganga'
}

# loop with key-value
for c, r in world_largest_rivers.items():
    print("The "+r.title()+" river runs "
          + "through " + c.title())

print("")
# loop with key
for c in world_largest_rivers.keys():
    print("Country: ", c)

print("")

# loop with value
for r in world_largest_rivers.values():
    print("rivers: ", r)
