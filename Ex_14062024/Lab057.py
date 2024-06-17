# Use of passing argument in function
def allowed_to_enter_website(username, password):
    if username == "admin" and password == "Yes":
        print("Access granted")
    else:
        print("Access denied")


allowed_to_enter_website("admin", "Yes")
allowed_to_enter_website("admin1", "Yes")
