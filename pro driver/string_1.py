str= "Hello world!"
r=input("Enter the term to replace:")
n=input("Enter the new term:")
l=len(str)
i=0
for i in range(l):
    if(str[i]==r):
        str[i]=n


