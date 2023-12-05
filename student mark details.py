print("Student mark details")
print("------- ---- -------")
name=input("Enter Student Name: ")
tamil=int(input("Enter Tamil mark: "))
english=int(input("Enter English Mark: "))
maths=int(input("Enter Maths Marks: "))
science=int(input("Enter science Marks: "))
social=int(input("Enter Social marks: "))
print("\nStudent Mark List Summary")
print("_______ ____ ____ _______")
#print("\n\n")
if tamil >= 50 and english >= 50 and maths >= 50 and science >= 50 and social >= 50:
    print("tamil mark: ", tamil)
    print("English mark: ", english)
    print("Maths mark: ", maths)
    print("Science mark: ", science)
    print("Social mark: ", social)
    total = tamil + english + maths + science + social
    average = total / 5
    print("Your total marks:", total)
    print("Your Percentage: ", average, "%")
else:
    print("You failed...study well")
'''
if tamil >= 50 and english >= 50 and maths >= 50 and science >= 50 and social >= 50:
    print("tamil mark: ", tamil)
    print("English mark: ", english)
    print("Maths mark: ", maths)
    print("Science mark: ", science)
    print("Social mark: ", social)
    total = tamil+english+maths+science+social
    average = total / 5
    print("Your total marks:", total)
    print("Your Percentage: ", average,"%")
else:
    print("You failed...study well")
    
    
    
    
      if avg >= 91 and avg <= 100:
        print("Your Grade is A1")
    elif avg >= 81 and avg < 91:
        print("Your Grade is A2")
    elif avg >= 71 and avg < 81:
        print("Your Grade is B1")
    elif avg >= 61 and avg < 71:
        print("Your Grade is B2")
    elif avg >= 51 and avg < 61:
        print("Your Grade is C1")
    elif avg >= 41 and avg < 51:
        print("Your Grade is C2")
    elif avg >= 33 and avg < 41:
        print("Your Grade is D")
    elif avg >= 21 and avg < 33:
        print("Your Grade is E1")
    elif avg >= 0 and avg < 21:
        print("Your Grade is E2")
    else:
        print("Invalid Input!")
'''