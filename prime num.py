n = int(input("enter a number"))
print("the entered value is:", n)
flag = True 
for i in range (2,n):
    if (n%i==0):
         flag = False
         break

if(flag== True):
     print("number is prime")
else:
      print("number is not prime")