print("                           ***************WELCOME***************")
print("\nPlease enter your username and password by paying attention to the uppercase and lowercase characters.\n")

username="user"
password="login"
attempt=3


while attempt>0:
    u=input("Username: ")
    p=input("Password: ")
    if u==username and p==password:
        print("\nSuccessful Login. You're redirected to homepage...")
        break
    elif u==username and p!=password:
        print("\nLogin failed. The password you entered is incorrect.")
        attempt-=1
    elif u!=username and p==password:
        print("\nLogin failed. The username you entered is incorrect.")
        attempt-=1
    else:
        print("\nLogin failed. The username and password you entered is incorrect.")
        attempt-=1
    if attempt>=1:
        print("Try again...\n")
    else:
        print("You did three mistakes! Attempt limit is exceeded.")
