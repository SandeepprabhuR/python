n=int(input("How many Multiplication tables you want: "))
if n>=0 and n<=1000:
    for i in range(1,n+1):
        n=n*1
        print(i)
        for j in range(1,11):
            print(j,"*",i,"=",(j*i))
else:
    print("Enter valid number")