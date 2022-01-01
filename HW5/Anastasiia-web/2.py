# Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

login_name = input('What is your name?')
# 1
while login_name in login_name == 'First':
    print('Hello')
    break
else:
    print('Error message')
    
# 2
if login_name == 'First':
    print('Hello')
else:
    print('Error message')

# 3
print('Hello') if login_name == 'First' else print('Error message')

# 4
check_user_name = print('Hello') if login_name == 'First' else print('Error message')

# 5
def check_user_name():
    print('Hello') if login_name == 'First' else print('Error message')

check_user_name()
    