import time

def check_eligibility():
    a = input("Do You Check Eligible For Vote (Type: Yes And No) ")
    
    if a.lower() == "yes":
        print("You Are Eligible For Please Choose Your Age:")
        print(" 1 : Age (1-10) ")
        print(" 2 : Age (10-15) ")
        print(" 3 : Age (15-17) ")
        print(" 4 : Age (18-100<) ")
        
        x = int(input("Enter The option 1-4: "))
        check_age(x)

    elif a.lower() == "no":
        print("Ok No problem")
        greeting_message()

    else:
        print("Your Input is Wrong")
        b = input("Are You Interested For Checking Eligibility For Vote : ")
        if b.lower() == "yes":
            check_eligibility()
        else:
            print("Thanks For Visiting!")

def check_age(age_option):
    if age_option == 1:
        print("Your Age Is 1-10. You Cannot Vote, You Are a Child. Enjoy playing games.")

    elif age_option == 2:
        print("Your Age Is 10-15. You Cannot Vote, You Are a Child. Enjoy playing games. You can drive only a cycle.")

    elif age_option == 3:
        print("Your Age Is 15-17. You Cannot Vote, You Are a Child. Enjoy playing games. You can drive only a scooter.")

    elif age_option == 4:
        print("Your Age Is 18-100. You Can Vote. You can drive.")

    else:
        print("Your input is wrong. Enter an option between 1-4.")

    greeting_message()

def greeting_message():
    tm = int(time.strftime('%H'))

    if 0 < tm < 12:
        print("Good Morning!")

    elif 12 <= tm < 13:
        print("Good Noon")

    elif 13 <= tm < 17:
        print("Good Afternoon!")

    elif 17 <= tm < 20:
        print("Good Evening!")

    elif 20 <= tm <= 24:
        print("Good Night")

    print("Thanks For Visiting!")

# Call the main function to start the program
check_eligibility()
