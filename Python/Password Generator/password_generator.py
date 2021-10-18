# importing string module for the alphabets
import string

# importing random module for getting the random number
import random

# list for the alphabets and numbets to create a password from.
passw = []

# appending alphabets
for i in string.ascii_lowercase:
    passw.append(i)
for i in string.ascii_uppercase:
    passw.append(i)

# appending number 0-10
for i in range(10 + 1):
    passw.append(i)

# password for concatenating random letter and number
password = ""
for i in range(int(input("Enter how long you want the password : "))):
    letter = random.choice(passw)
    password += str(letter)
print(password)
