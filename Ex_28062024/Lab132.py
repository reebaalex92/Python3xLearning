class Password:
    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_password(self, auth):
        if auth:
            print(self.__password)
        else:
            print("Access Denied")

    def set_password(self, password):
        if password.endswith("9"):
            if len(password) >= 10:
                self.__password = password
                print("Password set correctly", self.__password)
        else:
            print("Password is weak password")


p = Password("reeba12345")
p.get_password(True)
p.set_password("reeba12567788989")
