amt=0
eu=int(input("Enter The Number Of Electricity Unit : "))
print("Your Electricity Unit Is ",eu)
if(eu<=100):
    print("Free Electricity No Need To Pay")

elif(eu>100) and (eu<200):
    amt=(eu-100)*5
    print("Your Electricity Bill Amount Is : ",amt)
else:
    amt=500+(eu-200)*10
    print("Your Electricity Bill Amount Is : ",amt)
    