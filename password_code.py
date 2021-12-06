
from cryptography.fernet import Fernet

#password storing code 
print("Thank you for using my program to store your password I assure you that this is a very safe way to store your password.")

master_pwd = input("\nChoose a master password, use this to encrypt your passwords and username: ")

#function 
'''
def write_key(): 
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file: 
        key_file.write(key) '''

def load_key(): 
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    pass 
    with open("password.txt" , 'r' ) as f: 
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.rsplit("|")
            print("User: ", user, "Password:", str(fer.decrypt(password.encode())))
        

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open ("password.txt" , 'a' ) as f: 
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

while True: 
    mode = input("What would you like to do? (add/view) or press q to quit:\n").lower()
    if mode == "q": 
        break

    if mode == "add": 
        add()
    elif mode == "view": 
        view()
    else:
        print("Invalid option")
        continue 



