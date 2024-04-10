pr=int(input("Enter The price : "))
tax=0
print("Your Price Is : ",pr)
if(pr>100000):
    tax=15/100*pr
    print("Your Tax IS : ",tax)
elif(pr>50000 and pr<=100000):
    tax=10/100*pr;
    print("Your Tax IS : ",tax)

else:
    tax=5/100*pr
    print("Your Tax IS : ",tax)