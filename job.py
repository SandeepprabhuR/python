print("Job Application")
print("--- -----------")
age=int(input("Enter your age: "))
name=input("Enter your Name: ")
gender=input("Enter your Gender: ")
city=input("Enter your City name: ")
qualification=input("Enter your qualification: ")
print("\n Status Summary for your application")
print(" ------ ------- --- ---- -----------")
if age>=20 and age<=30:
    print("Candiadate Name: ", name)
    print("Candidate qualification: ", qualification)
    print("candidate age: ", age)
    #print("You are eligible for this job")
else:
    print("Your Age limit be exceed..Thank")
if 'female' in gender:
    print("gender: ", gender)
else:
    print("This job only for female candidates")
if 'madurai' in city:
    print("city: ", city)
    print("You are eligible for this job..Congrats")
else:
    print("This job only madurai city candipython seconddates")
