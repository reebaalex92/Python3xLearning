# Match in python
# Match for integer
# matches the given input with case.case _ mentions the default case.
numbers = int(input("Enter a number\n"))
match numbers:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("Invalid number")

#  Match for string
# matches the given input with case.case _ mentions the default case.
name = input("Enter a name\n")
match name:
    case "Reeba":
        print("Hello I am Reeba")
    case "Radhika":
        print("Hello I am Radhika")
    case _:
        print("Invalid name")

# Match for browser testing
browser = input("Enter a browser name\n")
browser = browser.capitalize()
match browser:
    case "Edge":
        print("Edge code is executed")
    case "Chrome":
        print("Chrome code is executed")
    case "Firefox":
        print("Firefox code is executed")
    case _:
        print("Invalid browser")



