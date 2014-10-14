#Tony K.
#23/09/2014
#Spot check

whole_number= int(input("Please enter your integer of grams: "))

hundred = whole_number // 100
remainder1 = whole_number % 100

fifty = remainder1 // 50
remainder2 = remainder1 % 50

ten = remainder2 // 10
remainder3 = remainder2 % 10

five = remainder3 // 5
remainder4 = remainder3 % 5

two = remainder4 // 2
remainder5 = remainder4 % 2

one = remainder5 / 1

print("{0} grams goes into {1}x100g, {2}x50g, {3}x10g, {4}x5g, {5}x2g and {6}x1g".format(whole_number,hundred, fifty, ten, five, two, one))
