def pal(n):
    m=n
    rev=0
    while(n!=0):
        r=n%10
        rev=(rev*10+r)
        n=n//10
    print(rev)
    if(rev==m):
        print("It is palindrome")
    else:
        print("It is not palindrome")
num=int(input("Enter a number"))
pal(num)