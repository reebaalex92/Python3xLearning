class VwoLoginPage:
    email = None
    password = None

    def __init__(self, o_email, o_password):
        self.email = o_email
        self.password = o_password

    def login_confirm(self):
        if self.password == "abc123":
            print("Login Successful")
        else:
            print("Login Failed")


reeba = VwoLoginPage("reeba123@gmail.com", "abcd")
reeba.login_confirm()
print("*************")
john = VwoLoginPage("john@gmail.com", "abc123")
john.login_confirm()


