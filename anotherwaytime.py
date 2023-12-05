import datetime
namelist=[]
agelist=[]
placelist=[]
name=input("Enter the name: ")
age=input("Enter the Age: ")
city=input("Enter the place: ")

while name!="" and age!=0 and city!="":
    time=datetime.datetime.now().strftime("%H:%M:%S")
    name+="\t\t\tTime: "+time
    namelist.append(name)
    name=input("Enter the Name: ")
    
    time=datetime.datetime.now().strftime("%H:%M:%S")
    age+="\t\t\t\tTime: "+time
    agelist.append(age)
    age=input("Enter the Age: ")
 
    time=datetime.datetime.now().strftime("%H:%M:%S")
    city+="\t\t\tTime: "+time
    placelist.append(city)
    city=input("Enter the Place: ")
print("Show Datas:")
print("---------------------------------------------------------------")
for i in range(0,len(namelist)):
    print("person ",(i+1),"Name : ",namelist[i])
    print("person ",(i+1),"Age  : ",agelist[i])
    print("person ",(i+1),"Place: ",placelist[i])
print("---------------------------------------------------------------")
