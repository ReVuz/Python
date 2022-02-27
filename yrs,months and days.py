#Enter days and display to yrs, months and days
d=int(input("Enter number of days "))
yrs=d/365
month=(d%365)/12
da=((d%365)%12)/30
print(d," will have ",yrs," years, ",month," months and ",da," days")
