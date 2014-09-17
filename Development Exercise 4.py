#Tony K.
#16/09/2014
#Development Exercise 4

print("This program calculates the volume of a swimming pool.")

length = float(input("Please enter the length of the swimming pool in meters: "))
width = float(input("Please enter the width of the swimming pool in meters: "))
shallowest_depth = float(input("Please enter the shallowest depth of the swimming pool in meters: "))
deepest_depth = float(input("Please enter the deepest depth of the swimming pool in meters: "))

volume1 = shallowest_depth * length * width

volume2 = ((deepest_depth - shallowest_depth)* length * 0.5) * width

answer = volume1 + volume2

print("The amount of water required to fill the swimming pool is {0} meters cubed".format(answer))

if answer < 250:
    print("You are helping the enviroment, by not wasting much water.")

else:
    print("You are harming the enviroment, use less water!")

print("Thank you for using this programm.")



