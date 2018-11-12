n=int(input("enter the limit"))
rn=0
while(n!=0):
    r=n%10
    rn=(rn*10+r)
    n=n//10
print("Revised num",rn)
