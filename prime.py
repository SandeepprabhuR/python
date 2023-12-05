print("Prime Number Checking")
number = int(input("Enter the number: "))
if number > 1:
        if (number % 2==0 and number != 2):
            print(number," is not a prime number")
        else:
            print(number," is a prime number")
else:
    print(number," is a composite number, so enter another number")