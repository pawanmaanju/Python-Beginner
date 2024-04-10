
import time
a=input("Do You Check Eligible For Vote (Type: Yes And No ) : ")
if("Yes"==a or "yes"==a):
    print("You Are Eligible For Please Choose Your Age : ")
    print(" 1 : Age (1-10) ")
    print(" 2 : Age (10-15) ")
    print(" 3 : Age (15-17) ")
    print(" 4 : Age (18-100<) ")
    x=int(input("Enter The option 1-4 : "))
    match x:
        case 1:
            print("Your Age Is 1-10 You Can Not Vote Your Are Child ")
            print("You Playing Game ")
        case 2:
            print("Your Age Is 10-15 You Can Not Vote Your Are Child ")
            print("You playing Game ")
            print("Tou Can Drive  Only Cycle")
        case 3:
            print("Your Age Is 15-17 You Can Not Vote Your Are Child ")
            print("You playing Game ")
            print("Tou Can Drive  Only ScOOty")
        case 4: 
            print("Your Age Is 18-100 You Can Not Vote Your Are Child ")
            print("Tou Can Drive ")
        case _:
            print("Your input is Wrong Enter 1-4 Between ")
    tm=int(time.strftime('%H'))
     # print(tm)
    #tm= int(input("Enter The Time "))
    if (tm>0 and tm<12):
        print("Good Morning!")
    elif(tm>=12 and tm<13):
        print("Good Noon")
    elif(tm>=13 and tm<17):
        print("Good Afternoon!")
    elif(tm>=17 and tm<20):
        print("Good Evening!")
    elif(tm>=20 and tm<=24):
        print("Good Night")
    print("Thanks For Visiting! ")     
elif("No"==a or "no"==a):
     print("Ok No problem")
     tm=int(time.strftime('%H'))
     # print(tm)
     #tm= int(input("Enter The Time "))
     if (tm>0 and tm<12):
        print("Good Morning")
     elif(tm>=12 and tm<13):
        print("Good Noon")
     elif(tm>=13 and tm<17):
        print("Good Afternoon")


     elif(tm>=17 and tm<20):
        print("Good Evening")

     elif(tm>=20 and tm<=24):
        print("Good Night")
     print("Thanks For Visiting! ")
else:
    print("Your Input is Wrong")
    b=input("Are You Interest For Check Eligible For Vote : ")
    if("Yes"==b or "yes"==b):
        print(a);
    
    else:
        print("Ok No problem  ");
        print("Thanks For Visiting");


