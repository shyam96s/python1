def largest(n1,n2,n3):
    if(n1>n2 and n1>n3):
         print(str (n1)+" is the largest")


   
    elif(n2>n1 and n2>n3 ):
        print(str (n2)+" is the largest")
    
    else:
        print(str (n3)+" is the largest")
    
x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))
largest(x,y,z)
    
