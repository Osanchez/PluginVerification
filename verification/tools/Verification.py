import hashlib
import uuid


def hash_id(id):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + id.encode()).hexdigest() + ':' + salt


def check_id(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Please enter a password: ')
hashed_password = hash_id(new_pass)

print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')

if check_id(hashed_password, old_pass):
    print('Correct Hashkey')
else:
    print('Incorrect Hashkey')
