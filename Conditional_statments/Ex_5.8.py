#Example 5.8
user_names = ['osama','faizan','mustufa','admin','zawar','ali','hamza','moiz']

for user_name in user_names:
    if user_name == 'admin':
        print('Hello '+str(user_name)+', would you like to see a status report?\n')
    else:
        print('Hello '+str(user_name)+', thank you for logging in again.\n')