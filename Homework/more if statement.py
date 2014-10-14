#Tony K.
#23/09/2014
#More if statement

def main():
    number = int(input("Please enter a number between 1 to 20: "))
    if number >=20:
             print("Your number is too high")
    elif number < 0:
                 print("Your number is too low")
    else:
        print("You are within range")
