subject=[]
for i in range(5):
    m=int(input("Enter the subject "+str(i+1)+" mark: "))
    subject.append(m)
total=sum(subject)
avg=total/5
for i in range(5):
    mark=subject[i]
    if mark>90 and mark<=100:
        print("subject",(i+1),"A Grade")
    elif mark>80 and mark<=90:
        print("subject",(i+1),"B Grade")
    elif mark>70 and mark<=80:
        print("subject",(i+1),"C Grade")
    elif mark>60 and mark<=70:
        print("subject",(i+1),"D Grade")
    elif mark>50 and mark<=60:
        print("subject",(i+1),"E Grade")
    else:
        print("subject",(i+1),"FAIL")
print("Total MArks   :",total)
print("Average MArks :",avg)


