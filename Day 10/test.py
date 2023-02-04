# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
#
# def my_function(num1, num2 ):
#     return num1 * num2
#
# output = my_function(num1, num2)
#
# print(output)

# test 1

def format_name(fname, lname):
    """Take First name Last Name
     and format it as a title text"""
    return fname.title() + " " + lname.title()


print(format_name(input("Enter First Name: "), input("Enter Last Name: ")))

