# Describe what the program does.
print("\nPurchasing Food")
print("===============\n")
print("Description: A simple program that asks the user for the total amount of Gummies they would like to buy. Prices are listed with and without VAT.\n")

# Define variables.
gummiesCost = float(0.50)
vat = float(20)
costFormatter = '.2f'

# 1) Get input from the user.
# The user will enter how many gummies they want.
print("Each Gummie costs: £", format(gummiesCost, costFormatter))
prompt = "How many Gummies would you like? "
gummiesAmount = int( input(prompt) )

# 2) Display the total amount of gummies.
# Multiply the gummies cost (without vat) by the total amount of gummies wanted.
totalCostMinusVat = gummiesAmount * gummiesCost
print("The total cost minus VAT is: £", format(totalCostMinusVat, costFormatter) )

# 4) Display the total vat. 
# The forumula calculates the vat of the total amount of gummies.
# calculatePercentage() is a reusable function, which in this case, calculates vat.
def calculatePercentage(percent, whole):
  return  (percent * whole) / 100.0 

totalVat = calculatePercentage(vat, totalCostMinusVat)
print("The VAT is: £", format(totalVat, costFormatter))

# 4) Display the total cost of gummies with vat added.
# Simply add the totals together to give us our total cost.
totalCostWithVat = totalVat+totalCostMinusVat
print("The total amount with VAT applied is: £", format(totalCostWithVat, costFormatter) )
