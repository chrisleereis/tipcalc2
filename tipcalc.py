print("Booted Tip Calculator...")
print("Please note that all numeric values must be typed in as a whole number.")
intro=input("Press Return to continue.")

#### EMPLOYEE INFORMATION ####

# craig's info
craig=input("Craig hours?")
craig=int(craig)
# loren's info
loren=input("Loren hours?")
loren=int(loren)
# tara's info
tara=input("Tara hours?")
tara=int(tara)
# saucy's info
saucy=input("Sazurice hours?")
saucy=int(saucy)


# adding total hours
totalhours=int(craig+loren+tara+saucy)
print("Thank you.")
print("...")
print("...")
print("...")
print(totalhours,"total hours")
# total amount of money collected
amountcollected=input("Total $ Tips?")
amountcollected=int(amountcollected)
print("working...")
print("...")
print("...")
print("...")

#### TIP REPORT ####

print("TIP REPORT")
print(totalhours,"total hours logged")
print("$",amountcollected,"total dollars tipped")
tiprate=(amountcollected/totalhours)
print("rate of $",tiprate,"per hour")
print("...")

#### RATE INFORMATION ####
#### make sure to update this info upon adding or removing employees ####

rate1=craig*tiprate
rate2=loren*tiprate
rate3=tara*tiprate
rate4=saucy*tiprate

#### RESULTS ####

print("Craig... $",int(rate1))
print("Loren... $",int(rate2))
print("Tara... $",int(rate3))
print("Sazurice...$",int(rate4))

#### REFERENCE DATA ####

addup=int(rate1+rate2+rate3+rate4)
deviance=int(amountcollected-addup)
print("...")
print("Initial amount was $",amountcollected)
print("Divisible amount was $",addup)
print("Final amount deviates from divisible amount by $",deviance)
print("...")
print("END OF REPORT")
