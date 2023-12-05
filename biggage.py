print("Bigger Aged People")
print("====== ==== ======")
name1=(input("Enter the name of first person: "))
person1=int(input("Enter the age of first person: "))
name2=(input("Enter the name of second person: "))
person2=int(input("Enter the age of second person: "))
name3=(input("Enter the name of third person: "))
person3=int(input("Enter the age of third person: "))
if person1 > person2 and person1 > person3:
    print("Name: ",name1)
    print("age:",person1)
    print("oldest man")
    print("=================")

elif person2 > person1 and person2 > person3:
    print("Name: ", name2)
    print("age:", person2)
    print("oldest Man")
    print("=================")

else:
    print("Name: ", name3)
    print("age:", person3)
    print("Oldest man")
    print("=================")

if person1 < person2 and person1 < person3:
    print("Name: ", name1)
    print("age:", person1)
    print("youngest man")
    print("=================")

elif person2 < person1 and person2 < person3:
    print("Name: ", name3)
    print("age:", person3)
    print("Youngest man")
    print("=================")
else:
    print("Name: ", name3)
    print("age:", person3)
    print("Youngest Man")
    print("=================")
