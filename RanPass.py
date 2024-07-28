import random
import string

def generate_password(length=12):
    print("Do you want to generate a password for yourself? (yes/no)")
    user_input = input('Enter: ').strip().lower()
    
    if user_input == 'yes':
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    else:
        print('Thank you!')
        return ''

# Example usage
password = generate_password()
if password:
    print('Your password is:', password)
