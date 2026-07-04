num=int(input("Enter the number:"))
if num < 0:
    if num % 2 == 0:
        print("The Number is Negative and Even!")
    else:
        print("The Number is Negative and Odd!")
elif num > 0:
    if num % 2 == 0:
        print("The Number is Positive and Even!")
    else:
        print("The Number is Positive and Odd!")
else:
    print("The Number is 0!")
