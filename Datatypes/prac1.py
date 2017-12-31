
squares = []

for value in range(1,11):
    squares.append(value*3)

print(squares)

print()

squares = [value*3 for value in range(1,11)]

print(squares)

even = [value for value in range(1,21) if value % 2 == 0]
print(even)