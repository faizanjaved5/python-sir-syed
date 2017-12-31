# Example 5.11

ordinal_numbers = []
for num in range(1, 11):
    ordinal_numbers.append(num)

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(str(ordinal_number) + 'st')
    elif ordinal_number == 2:
        print(str(ordinal_number) + 'nd')
    elif ordinal_number == 3:
        print(str(ordinal_number) + 'rd')
    else:
        print(str(ordinal_number) + 'th')
