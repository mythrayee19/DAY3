#DAY3 ASSIGNMENT 1
for alt in range(1000,10000):
    alt=int(input("Enter the Altitude:"))
    if alt==1000:
        print("Safe to Land")
    elif alt>1000 and alt<5000:
        print("Bring down to 1000")
    else:
        print("Turn Around")

        
#OUTPUT:
## Enter the Altitude:1000
##Safe to Land
##Enter the Altitude:4500
##Bring down to 1000
##Enter the Altitude:6500
##Turn Around
##Enter the Altitude:
