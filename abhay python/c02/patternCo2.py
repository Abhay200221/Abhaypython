x=int(input("Enter the limit"))
for i in range(0,x):
    for j in range(0,i):
        print("*" ,end=" ")
    print("\n")
for i in range(0,x):
    for j in range(i,x):
        print("*" ,end=" ")
    print("\n")
