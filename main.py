"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
numCharInput = int(input("How many characters? "))
woodInput = input("What type o wood?:\n1. Pine\n2. Oak (Additional $20)\n")
colorInput = input("Which color would you like?:\n1. Black\n2. White\n3. Gold (Additional $15)\n")

charge = 0.00
woodType = int(woodInput)
color = int(colorInput)

# The charge for all signs is a minimum of $35.00.
charge = 35

# Calculate additional charge for characters beyond 5
if numCharInput > 5:
    charge += (numCharInput - 5) * 4

# If the sign is made of oak, add $20.00. No charge is added for pine.
if woodType == 2:  # Checking if woodType equals 2 (Oak)
    charge += 20

# Black or white characters are included in the minimum charge; there is an additional $15 charge for gold-leaf lettering
if color == 3:  # Checking if color equals 3 (Gold)
    charge += 15

print("The charge for this sign is $" + str(charge))
