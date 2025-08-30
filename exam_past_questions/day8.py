

# Write a program that:
# Total 30 Marks
# (a)
# (b)
# Incorporates a user defined function (called checkPassword(password)) to determine
# if
# a password is
#  a good password. A password is defined as being a
#  good password if
# it is
#  at least 8 characters long and contains at least one uppercase letter, one lowercase
# letter and at least one number. (10 Marks)
# Your function should return true if the password passed to it as it's only parameter is
# good. Otherwise, it should return false.
# (c) If
#  the checkPassword function returns a false value then it should indicate why it
#  is
# (5 Marks)
# returning a false value. (10 Marks)
# (d) Include a main programme that reads a password from the user and reports whether
# or not it
#  is good.


# define function
# accept input password and hold in variable
# if password legnth is 8 
# password.len === 8 and password contains special char
# acters and uppercases
# is is good
# else
# print
#
#def main():


def checkPassword(password):
   reason = [] 
   if len(password) < 8:
        reason.append("Password must be at least 8 characters long.")
   elif not any(char.isupper() for char in password): 
        reason.append("Password must contain at least one uppercase letter.")
   elif not any(char.islower() for char in password): 
        reason.append("Password must contain at least one uppercase letter.") 
   elif not any(char.isdigit() for char in password):
        reason.append("Password must contain at least one number.")
   elif not reason:
        return True, ["password is good"]
   else: 
        return False, reason           
   

def main():
    password = input("Enter a password:")   
    is_good, message   = checkPassword(password)

    if is_good:
        print("Password is good.")
    else:
        print("Password is not good.")
        for reason in message:
            print(" -", reason)


if __name__ == "__main__":
    main()    



