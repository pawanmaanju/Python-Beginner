# This Method Use For Check End With Same latter Then Print TRUE Another Print FALSE
Name=input("Enter Your Name  : ")
print("Your Name END WITH 'a' Word is : ",Name.endswith("a"))
print("Your Name END WITH 'n' Word is : ",Name.endswith("n"))

#Check Provide Index Start Number And End Number 

print("Your Name END WITH 'n' Star - '1' End - '3' Word is : ",Name.endswith("n",2,4))
print("Your Name END WITH 'n' Star - '3' End - '5' Word is : ",Name.endswith("n",3,5))

