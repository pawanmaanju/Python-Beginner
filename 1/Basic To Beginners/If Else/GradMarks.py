per = float(input("Enter Your Percentage : "))
if(per>100):
    print("Wrong Percentage")
elif(per>=99):
    print("Your Are Genius With 'A+' Grade ")
elif(per>90):
    print("Very Good With 'A' Grade ")
elif(per>80 and per<=90):
    print("Good With 'B' Grade ")
elif(per>60 and per<=80):
    print("Average With 'C' Grade ")
elif(per>50 and per<=60):
    print("Poor With 'D' Grade ")
elif(per<=50):
    print("Fail With 'E' Grade ")

# 2nd way 

# percentage = float(input("Enter Your Percentage: "))

# if percentage > 100:
#     print("Wrong Percentage")
# else:
#     grades = {
#         90: "A",
#         80: "B",
#         60: "C",
#         50: "D"
#     }
#     grade = next((grade for cutoff, grade in grades.items() if percentage >= cutoff), "E")
#     if percentage >= 99:
#         grade += "+ (Genius)"
#     print(f"You got a {grade} grade.")
