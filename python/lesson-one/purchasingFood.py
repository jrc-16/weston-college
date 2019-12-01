# Define variables
gummiesCost = float(0.50)
vat = float(20)
costFormatter = '.2f'

# 1) Take input from the user
# the user will enter how many gummies they want
# the program needs to use the value to multiply 0.50
gummiesCost = float(0.50)
vat = float(20)
costFormatter = '.2f'
print("Gummies cost: £", format(gummiesCost, costFormatter))
prompt = "How many gummies would you like? "
gummiesAmount = int( input(prompt) )

# 2) Display the total amount (totalNoVat)
# the program needs to display the total amount to the screen
# this amount is the total wihtout vat
totalCostMinusVat = gummiesAmount * gummiesCost
print("The total cost minus vat is: £", format(totalCostMinusVat, costFormatter)    )

# 4) Write the forumula that calculates the vat of the total amount of gummies

def calculatePercentage(percent, whole):
  return  (percent * whole) / 100.0 

totalVat = calculatePercentage(vat, totalCostMinusVat)
print("The VAT is: £", format(totalVat, costFormatter))

# 4) Display the total amount with vat applied (totalWithVat)
# the program needs to calculate the vat of the total amount of gummies
totalCostWithVat = totalVat+totalCostMinusVat
print("The total amount with vat applied is: £", format(totalCostWithVat, costFormatter) )
