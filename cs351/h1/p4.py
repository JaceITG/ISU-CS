import sys

bit_positions = []
#Loop through args to convert to int and add to list of bit positions
for arg in sys.argv[1:]:
    bit_positions.append(int(arg))

#Create a binary literal
num = 0b0

#Go through each of the positions that need to be set to 1
for pos in bit_positions:
    #bit shift a 1 to the position we want to set
    ##EX:  for position 3 we bit shift a 1 to the left 3 times: 1000
    bit = 0b1 << pos

    #"or" the bit with our binary literal, ensuring the bit at that position
    #becomes set, while leaving the rest of the int in tact
    num = num|bit

#Print the binary, hex, and decimal representations
print(format(num,'032b') + " " + format(num,'08X') + " " + str(num))
