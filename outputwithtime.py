import datetime
namelist=[]
agelist=[]
placelist=[]
name=input("Enter the name: ")
while name!="":
    time=datetime.datetime.now().strftime("%H:%M:%S")
    name+="\tTime: "+time
    namelist.append(name)
    name=input("Enter the Name: ")
age=input("Enter the Age: ")
while age!="":
    time=datetime.datetime.now().strftime("%H:%M:%S")
    age+="\t        Time: "+time
    agelist.append(age)
    age=input("Enter the Age: ")
city=input("Enter the place: ")
while city!="":
    time=datetime.datetime.now().strftime("%H:%M:%S")
    city+="\t       Time: "+time
    placelist.append(city)
    city=input("Enter the Place: ")

print("Show Datas:")
for i in range(0,len(namelist)):
    print("person ",(i+1),"Name: ",namelist[i])
print("=================================================")
for i in range(0,len(agelist)):
    print("person ",(i+1),"Age: ",agelist[i])
print("=================================================")
for i in range(0,len(placelist)):
    print("person ",(i+1),"Place: ",placelist[i])
print("=================================================")
