import random

numbers = "0123456789"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
symbols = "[]{}()*;/,._-"

# Add the number, character and symbols
sum = lower + upper + numbers + symbols

# Ask the user to enter length of the password
length = int(input("Enter the password length: "))

# Shuffle the password
shuffle = random.sample(sum, int(length))

# Convert list to string
password = "".join(shuffle)

print(password)
