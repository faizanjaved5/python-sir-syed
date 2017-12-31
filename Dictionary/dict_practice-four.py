# Practice of Dictionary Data-Structure

# looping through key-value pair of dictionary

user_info = {
    'username': 'kosama',
    'first': 'osama',
    'last': 'khan',
}

favorite_languages = {
    'osama': 'python',
    'mustufa': 'c',
    'zawar': 'ruby',
    'faizan': 'java script',
    'ali': 'c#',
    'hamza': 'php'
}

# print key and value of user_info
for k, v in user_info.items():
    print("\nKey: ", k)
    print("Value: ", v)

print("\n")

# print all the favourite langauges dictionary key and value with a message
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
