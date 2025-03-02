from cryptography.fernet import Fernet
# Fernet is a symmetric algorith that deploys the same key for encrypt and decrypt of data
# The Cryptography module must be installed in order to use Fernet
masterpass = input('Please type the master password: ')

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
# The key is generated and stored in a file called key.key

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

masterpass = input('Please type the master password: ')
key = load_key() + masterpass.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print('User:', user, "| Password:", str(fer.decrypt(passw.encode())))
# data.split will display the data into "user" and "passw". If a third element existed, we need a third variable to split and show everything correctly.
#r is used to read the passwords in the txt file

def add():
    name = input('Account name:')
    pwd = input('Password:')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + str(fer.encrypt(pwd.encode())) + '\n')

        #a is used to append new passwords for the txt file or create one if it doesn't exist
while True:
    mode = input('Do you want to add a new password or view existing ones (view,add)? Press q to quit:').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()

    elif mode == 'add':
        add()
    else:
        print('Please enter a valid mode.')
    continue