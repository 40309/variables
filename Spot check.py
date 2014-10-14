#Tony K.
#23/09/2014
#Spot check

width= float(input("Please enter the width of the swimming pool: "))
length = float(input("Please enter the length of the swimming pool: "))
depth = float(input("Please enter the depth of the swimming pool: "))

mainSectionVolume= length*width*depth

circleRaidius= width/2

circleArea= 3.14*(circleRaidius*2)

halfCircleVolume= (circleArea/2)*depth

poolVolume= mainSectionVolume + halfCircleVolume

print(poolVolume)

