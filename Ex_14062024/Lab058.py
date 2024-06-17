# function using match
def allowed_enter_website(username):
    match username:
        case "admin":
            print("Access granted")
        case _:
            print("Access denied")


allowed_enter_website("admin")
allowed_enter_website("user1")