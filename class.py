class user:
    name = ''
    email= ''
    password = ''
    login = False


    def login(self):
        email = input("Enter email")
        password = input("Enter password")

        if email  == self.email and password == self.password:

            login = True
            print("Login succedfull")
        else:
            print("login Faild!")

    def logout(self):
        login = False
        print("logged out!")

    def isloggedIn(self):
        if self.login:
            return True
        else:
            print("user is not logged in !")

user1 =  user()

user1.name = "Tamim"
user1.email = "tamimkhan7133@gmail.com"
user1.password = "123456"
user1.login()



hello = input()
