import os

from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("private.key", "wb+") as encrypt_file:
        encrypt_file.write(key)
'''


def load_key():
    return open("private.key", "rb").read()


filename = 'password.txt'
# master password will be used for encryption
master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


# view existing usernames and passwords
def view():
    with open(filename, 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print(f'User: {user} | Password: {fer.decrypt(password.encode()).decode()}')


# Add new username and password
def add():
    name = input('Account Name: ')
    password = input("Password: ")
    with open(filename, 'a') as file:
        file.write(f'{name}|{fer.encrypt(password.encode()).decode()}\n')


# Find an account
def find(account_name: str) -> bool:
    is_account_present = False
    with open(filename, 'r') as file:
        if os.stat(filename).st_size == 0:
            print("File is Empty")
            exit()
        for line in file:
            name, _ = line.strip().split('|')
            if account_name.lower() == name.lower():
                is_account_present = True
                break
    return is_account_present


# Delete an account
def delete():
    name = input('Please enter the name of the account you want to delete: ')
    if find(name):
        with open(filename, 'r') as file:
            lines = file.readlines()
        print('Account exists', name)
        password = input('Enter the password: ')
        account = f'{name.lower()}|{password}'
        if verify_account(name, password):
            with open(filename, 'w') as file:
                file.seek(0)
                file.truncate()
                for line in lines:
                    if line.strip().lower() != account:
                        file.write(line)
                print("Account Deleted")
        else:
            print("Incorrect Password")
    else:
        print('Account not found')


def verify_account(account_name: str, password: str) -> bool:
    verified = False
    with open(filename, 'r+') as file:
        for line in file:
            name, pwd = line.strip().split('|')
            if account_name.lower() == name.lower() and pwd == password:
                verified = True
                break
    print("Account Verified")
    return verified


# Check if the file is empty or not
def has_record():
    return os.stat(filename).st_size != 0


while True:
    mode = input("Would you like to add a new password or view existing one (view, add, del)? ")
    if mode.lower() in ['q', 'quit', 'exit']:
        break
    if mode == "view" and has_record():
        view()
    elif mode == "add":
        add()
    elif mode == "del" and has_record():
        delete()
    else:
        print("Invalid mode.")
        continue
