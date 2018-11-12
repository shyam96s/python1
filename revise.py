def rev(a):
    rn=0
    while(a!=0):
         r=a%10
         rn=(rn*10+r)
         a=a//10
    return rn     
n=int(input("Enter a number"))
result=rev(n)
print(result)   


