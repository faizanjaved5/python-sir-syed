#Example 5.10

current_users = ['osama','moiz','faizan','ali','haris']
new_users = ['faizan','zawar','ali','mustufa','hamza']

for new_user in new_users:
    if new_user in current_users:
        print('you will need to enter anew username')
    else:
        print('username is available')