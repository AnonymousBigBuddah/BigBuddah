master_pwd = input("What is the master password?: ")

def view():
    with open('passwords.txt', 'r') as f:
        print('-- ------- --')
        for line in f.readlines():
            print(line.rstript())

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + " " + pwd + '\n')

while True:
    mode = input("Would you li(ke to add a new password or view existing ones ( view, add, q for quit) ")
    if mode.lower() == "q":
        break
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    else:
        print("Invalid mode.")

1:21:56