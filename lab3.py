
"""WAP to find out electricity bill for a user 

  Take month wise units of consumptions

 User types are : Household user/business user/ industrial user

 Rate per unit : Household: 2 rs / business: 5 rs / Industrial : 10 rs."""

print("1.household purpose\n2.Small Business purpose \n3.Industrial purpose :")
user_type=int(input("Enter the option:"))
e_unit=int(input("Consumption unit in a month:"))
print("Eletricity bill...")
if(user_type==1):
    bill=(2*e_unit)
    print("your bill is:",bill)
elif(user_type==2):
    bill=(5*e_unit)
    print("your bill is:",bill)
elif(user_type==3):
    bill=(10*e_unit)
    print("your bill is:",bill)


"""WAP to find out fare  for a user 

  Take KM wise  distance travelled as input

 Rate per KM : (0 to 10 ): 10 rs / (10-20 ): 5 rs / (above 20 ) : 4 rs."""


distance=int(input("Enter the travelled distance:"))
charges=0
if(distance<=10):
    charges=(10*distance)
elif(distance<=20):
    charges=(5*distance)
elif(distance>20):
    charges=(4*distance)

print("your travlled charges is:",charges)