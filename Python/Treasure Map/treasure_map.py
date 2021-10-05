# Location to store your treasure
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# Function that return user choice
def userChoice():
    check = ""
    acceptableRange = [11, 12, 13, 21, 22, 23, 31, 32, 33]

    # Check for digit
    while check.isdigit() == False:

        # Asking the user to store your treasure
        position = input("Where do you want to put the treasure [1-3][1-3]: ")

        # Check for acceptable range
        if position.isdigit() == False:
            print("Please enter the numerical value!")
        else:
            if int(position) not in acceptableRange:
                print("Please enter the acceptable range [1-3]][1-3]")
            else:
                check = position
    return position


# Storing result in desirable location
result = userChoice()
x = int(result[0])
y = int(result[1])

map[x - 1][y - 1] = "X"

# Printing Result
print(f"{row1}\n{row2}\n{row3}")
