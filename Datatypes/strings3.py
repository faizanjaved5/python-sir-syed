
#whitespaces to strings


#\n change to newline and \t give tab space
languages = "\n\tPython\n\tJava\n\tC\n\tC#\n\tjavascript"

message = "these are the languages i learned: "+languages

print(message.title())


#to remove extra spaces or spaces that we don't know are in strings
striper = "  Hello World   "

print(striper)
#strip functions remove extra spaces from both side
print(striper.strip())
#lstrip functions remove extra spaces from left side
print(striper.lstrip())
#rstrip functions remove extra spaces from right side
print(striper.rstrip())
