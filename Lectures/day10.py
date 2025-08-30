for num in range(2, 16, 5): 
    print(num)


# steps = 5

mystr = 'yes'
yourstr = 'no'
mystr += yourstr * 2
print(mystr)


special = "1357 Country Ln"
s_string = special[ :4]   # Extracting the first four characters
s_string2 = special[4: ]  # Extracting characters from index 4 to 9
print(s_string2)


ages = {'Aaron' : 6, 'Kelly' : 3, 'Abigail' : 1 }



# Write a program that:
# (a) Incorporates a user defined function (called checkPassword(password)) to determine
# if a password is a good password. A password is defined as being a good password if
# it is at least 8 characters long and contains at least one uppercase letter, one lowercase
# letter and at least one number. (8 Marks)
# (b) Your function should return true if the password passed to it as its only parameter is
# good. Otherwise, it should return false. (2 Marks)
# (c) If the checkPassword function returns a false value then it should indicate why it is
# returning a false value.
# (5 Marks)
# (d) Include a main programme that reads a password from the user and reports whether
# or not it is good.
# (5 Marks)


name = "sandra"
upperCase = name.upper()

#number of char
numChars = len(name)
print(f"Number of characters in {name} is {numChars}")


createNewUser = {
     "password": "aneal",
     "email": "aneal@example.com"
} 

#check if password contains number
iscontains = any(char.isdigit() for char in createNewUser["password"])

print(f"Password contains number: {iscontains}")