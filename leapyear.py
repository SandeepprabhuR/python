print("Leap year checking")
year=int(input("Enter your year: "))
if year%4 ==0:
    print("Its a leap year")

    if year%400 ==0:
        print("Its a leap year")
    else:
        print("not a leap year")
else:
    print("No..Its Not a leap year")