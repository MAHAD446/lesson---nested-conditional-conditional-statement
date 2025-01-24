# take input of number of units consemed for the user
units = int(input(" please enter number of units you consumed :"))

# check conditions of units consumed
# then calculete amount and surcharge accordingly
# surcharge is the tax valus

# chceck for units less than 50
if(units < 50):
    amount = units * 2.60
    surcharge = 25

# check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 162.50 +  ((units - 100) * 5.26)
    suncharged = 45

# check for all the casses other than mentioned
# when units consemed are more than 200
else:
    amont = 130 + 162.50 + 526 + (( units - 200) * 8.45)

# calculate and display the total electricity bill
# total amount = amount + surcharge
total = amount + surcharge
print("/ne elactricity bill = %.2f %total")

