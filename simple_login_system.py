
class Login:
    def __init__(self):
        pass

    def register(self):
        file = open('Login.txt', 'w')
        username = str(input('Enter username: '))
        password = str(input('Enter password: '))
        file.write(username + ',' + password + '\n')
        file.close()

    def login(self):
        username_entered = str(input('Enter username: '))
        password_entered = str(input('Enter password: '))
        file = open('Login.txt', 'r')
        for row in file:
            field = row.split(',')
            username = field[0]
            password = field[1]
            lastchar = len(password) - 1
            password = password[0:lastchar]

            if username_entered == username and password_entered == password:
                print('Login correct')
            else:
                print('Login incorrect')

        file.close()


if __name__ == '__main__':
    login = Login()

    while True:
        login_or_register = str(input('Do yuo want to register or login [r/l] ? '))
        if login_or_register == 'r':
            login.register()
        elif login_or_register == 'l':
            login.login()
