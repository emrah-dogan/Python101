#This program calculates the famous wheat and chessboard problem.

"""A grain of wheat is placed on the first square of the chessboard.
The amount of the wheat is increased two times on each square. 
An eight by eight chessboard has 64 squares.
2^0 + 2^1 + 2^2 + ... + 2^63 = ?"""

#Calculates 2^0 + 2^1 + 2^2 + ... + 2^63
base = 2
power = 0
total = 0
while power < 64:
    total = total + pow(base, power)
    power += 1

#Prints the number of grains to the console
print(total, " grains of wheat")

#Calculates and prints the amount of grains in metric tons (assuming that a wheat grain weighs nearly 0.65 mg)
total_in_tons = int((total * 0.65) / 10000000) 
print(total_in_tons, " tons of wheat")

#Annual global wheat production in metric tons in 2023
annual_global_production = 781310000

#Calculates and prints how much the total amount is bigger than the annual global production. 
times = int(total_in_tons / annual_global_production)
print("The total amount of wheat is ", times, "times more than the annual global production.")