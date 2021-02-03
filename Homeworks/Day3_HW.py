print("""
User login system....
""")

#define username and password so that input provided by the users can be checked
username = "edizkaraali"
password = "123456"

#define an entering right value to create safer system
entering_right = 3
while True:

 username_from_user = input("Please enter your username: ")
 password_from_user = input("Please enter your password: ")

 if (username_from_user == username) and (password_from_user != password):
    print("Password is incorrect, please enter a correct password!!")
    entering_right -= 1

 elif (username_from_user != username) and (password_from_user == password):
    print("Username is incorrect, please enter a correct username!!")
    entering_right -= 1

 elif (username_from_user != username) and (password_from_user != password):
    print("Both username and password are incorrect, please enter a correct username and password!!")
    entering_right -= 1

 else:
     print("Welcome to the system....")
     break

 #each time, check entering right
 if entering_right == 0:
     print("Your entering rights has been run off, please try again after 5 minutes...")
     break