class VWOLogin:

    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = "Reeba"


    def login_confirmation(self):
        if self.__email == "reeba@gmail.com" and self.__password == "reeba123":
            print("Login Successful")
        else:
            print("Login Failed")


r = VWOLogin("reeba@gmail.com", "reeba123", "reeba")
r.login_confirmation()
print(r.name)
