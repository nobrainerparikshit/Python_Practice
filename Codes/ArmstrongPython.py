num= int(input("Enter the Number:"))
sum=0
a = num
while a > 0:
    digi= a % 10
    sum+=digi ** 3
    a //= 10
if num == sum:
    print("This Number - ", num , "is an Armstrong Number!")
else:
    print("This Number - ", num , "is not an Armstrong Number!")
