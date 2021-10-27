#I dont see the relevance to the line "A Kilometer is 1/10000 of the distance between the North Pole and the Equator?

#initializing Kilometers defining degrees/min and nauticalmiles and taking an input for KM
Kilometers=int(input("Enter the number of kilometers: "))

degreesPerMin = 90*60

oneKm = degreesPerMin/10000

nauticalmile = oneKm*Kilometers

#printing the entered amount kilometers and the hopefully correct calculation for nautical miles
print (Kilometers,"km","is",nauticalmile,"Nautical miles")
