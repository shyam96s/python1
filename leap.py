def leap(n):
    if (n%4==0):

       if (n%100==0):

           if (n%400==0):

               print("{0} is a leap year".format(n))
           else:

               print("{0} is not a leap year".format(n))
       else:

           print("{0} is a leap year".format(n))
    else:

        print("{0} is not a leap year".format(n))
num=int(input("Enter an year"))
leap(num)