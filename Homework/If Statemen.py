#Tony K.
#23/09/2014
#If Statement, Selection R&R.md

print("This programm tells you if you are old enought to vote and retire")

user_age= int(input("Please enter your age: "))

if user_age >= 16:
    print ("You are old enough to vote")

else:
    print("You are not old enough to vote")


if user_age >= 65:
    retire_age= 65-user_age
    print("You have {0} until you can retire".format(retire_age))

else:
    print("You are not old enough to retire.")

print("Thank you for using my,(Tony's) programm!")
