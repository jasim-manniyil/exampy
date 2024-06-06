
i=1
n=5
for i in range(6):
    j=1
    for j in range(i):
        print(" "*n,end=" ")
        print("*",end=" ")
        n-=1
    print("\n")
    
for i in range(1,n+1,2):
    print()