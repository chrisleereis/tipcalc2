

##data
firstNames = ["Johnae", "Kayla", "Colin", "Kristen", "Edward", "Perry", "Angel", "Bry", "Tara", "Loren", "Naomi", "Asher", "Josh", "Chris Lee", "J.T.", "Vin", "Jasmine", "Sazurice", "Erica"]
lastNames  = ["Beckem", "Burress", "Campbell", "Dalen", "Dang", "Darling", "Dunne", "Ells", "Hadley", "Maxwell", "Moore", "Morris", "Packard", "Reis", "Schilling", "Tanner", "Weygand", "Williams", "Yoshimoto"]
partnerHour = []

print("Booted Tipcalculator 2.0")
print("Please enter the amount of hours each")
print("partner logged this week.")
print("...")
print("...")
print("...")

for firstName in firstNames:
    print(firstName, "hours?")
    partnerHour.append(int(input())) ## MAKE SURE THIS IS AN INPUT OF AN INTEGER!!
    ## figure out how the fuck to increase firstname[x] by 1 on every loop till end of range ## nvm i did it ## see integer comment above
    ## partnerHour=(partnerHour)
    totalhours=sum(partnerHour)


print("Amount in dollars collected?")
amountcollected=int(input())

totaltiprate=amountcollected/totalhours

tipratesperpartner = []
for partnerHours in partnerHour:
    tipratesperpartner.append(partnerHours*totaltiprate)
##tiprateperpartner=partnerHour*int(totaltiprate) ## make tiprateperpartner into an array 

##Report contents
print("")
print("TIP REPORT")
print("")
print(totalhours,"TOTAL HOURS")
print("$"+str(amountcollected),"AMNT COLLECTED")
print(totaltiprate,"TOTAL TIPRATE")
print("")

for firstName, tiprateperpartner in zip(firstNames,tipratesperpartner):
    print(firstName,int(tiprateperpartner))



