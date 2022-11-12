# Find if the given number is armstrong number
# If the given number base b is a number that is sum of digits raised to the power of no of dgits.
# Example 153 = 1*1*1+2*2*2+3*3*3, 1634=1*1*1*1+6*6*6*6+3*3*3*3+4*4*4*4

# Breakdown this program.
# Program-1: Find all the digits of a given number
""" n=143
temp=n; # Always copy the number before using in loop
# Why while loop?
while(temp!=0):
     rem = temp%10
     print(rem)
     #temp=temp/10 #what is wrong here?
     temp=temp//10

 """# Find the sum of all digits
n=140
sum=0 #Why?
temp=n; # Always copy the number before using in loop
# Why while loop?
while(temp!=0):
     rem = temp%10
     sum = sum*10+rem
     temp=temp//10 
print("sum of digits "+str(sum)) #Why str here?

# Find if given number is armstrong number

n=150
temp=n
sum=0
digits = 0
x=n
while (x != 0):
    digits = digits + 1
    x = x // 10
         
while (temp!=0):
    rem = temp%10
    sum = sum+ pow(rem,digits) # What happens if we call digits function?
    temp=temp//10

if(sum==n):
    print(str(n )+" is armstrog number")
else:
    print(str(n)+" is not an armstrong number")