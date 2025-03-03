from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    try:
        with open('key.key', 'rb') as file:
            key = file.read()
            print("Loaded key:", key)  # Debugging line to check the key
            return key
    except FileNotFoundError:
        print("Key file not found. Generating a new key.")
        write_key()
        return load_key()

key = load_key()
if len(key) != 44:  # Fernet keys should be 44 bytes long when base64-encoded
    raise ValueError("Invalid Fernet key length. Generated key is invalid.")

fer = Fernet(key)

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split('|')
                print('User:', user, "| Password:", fer.decrypt(passw.encode()).decode())
    except Exception as e:
        print("An error occurred while viewing passwords:", e)

def add():
    name = input('Account name:')
    pwd = input('Password:')
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

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