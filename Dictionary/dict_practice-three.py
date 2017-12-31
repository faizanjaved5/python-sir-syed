# Practice of Dictionary Data-Structure

# Modify Dictionary Value

formula_one = {'distance': 0, 'y_position': 25, 'speed': 'medium'}

print("Initial distance covered: " + str(formula_one['distance']))
# formula_one['speed'] = 'fast'
# Determine how far to move the car based on its current speed.
if formula_one['speed'] == 'slow':
    distance = 1
elif formula_one['speed'] == 'medium':
    distance = 2
else:
    # This must be a fast car.
    distance = 3


# The new position is the old position plus the increment.
formula_one['distance'] = formula_one['distance'] + distance

print("Now distance covered: " + str(formula_one['distance']))
