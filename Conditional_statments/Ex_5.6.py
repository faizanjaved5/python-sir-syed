#Example 5.6

age = int(input("Enter Your Age: "))


if age < 2:
    print('person is baby')
elif age < 4:
    print('person is toodler')
elif age < 13:
    print('person is kid')
elif age < 20:
    print('person is teenager')
elif age < 65:
    print('person is an adult')
elif age >= 65:
    print('person is an elder')