#Convert time entered in seconds to hrs ,mins and seconds
t=int(input("Enter time in seconds "))
hrs=t/3600
secs=t%3600
mins=secs/60
print("Time in hours : ",hrs,"\nseconds : ",secs,"\nminutes : ",mins)
