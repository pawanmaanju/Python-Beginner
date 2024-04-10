import time
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


else:
    print("Wrong Time!")



