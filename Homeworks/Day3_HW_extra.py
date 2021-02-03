print("""
User login system....
""")

#define username and password so that input provided by the users can be checked
username_password = {"edizkaraali" : "123456"}

#define an entering right value to create safer system
entry_right = 3

#store the incorrect entry values
wrong_entries = dict()

while True:

 username_from_user = input("Please enter your username: ")
 password_from_user = input("Please enter your password: ")

 if (username_from_user == list(username_password.keys())[0]) and (password_from_user != username_password.get("edizkaraali")):
    print("Password is incorrect, please enter a correct password!!")
    wrong_entries[username_from_user] = password_from_user
    entry_right -= 1

 elif (username_from_user != list(username_password.keys())[0]) and (password_from_user == username_password.get("edizkaraali")):
    print("Username is incorrect, please enter a correct username!!")
    wrong_entries[username_from_user] = password_from_user
    entry_right -= 1

 elif (username_from_user != list(username_password.keys())[0]) and (password_from_user != username_password.get("edizkaraali")):
    print("Both username and password are incorrect, please enter a correct username and password!!")
    wrong_entries[username_from_user] = password_from_user
    entry_right -= 1

 else:
     print("Welcome to the system....")
     break

 #each time, check entry right
 if entry_right == 0:
     print("Your entering rights has been run off, please try again after 5 minutes...")
     print("These are the entires that you have tried: ")
     for i,j in wrong_entries.items():
       print("Username:",i,"Password:",j)
     break
