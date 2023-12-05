import datetime
namelist=[]
name=input("Enter the name: ")
while name!="":
    time=datetime.datetime.now().strftime("%H:%M:%S")
    name+="\tTime: "+time
    namelist.append(name)
    name=input("Enter the Name: ")

print("Show Datas:")
for i in range(0,len(namelist)):
    print((i+1),namelist[i])