p = float(input("Enter the Principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the total time taken in months: "))
n = float(input("Enter the times of interest applied per time period: "))
si = (p * r * t) / 100
amount = p * (1 + (r / (100 * n)))**(n * t) 
ci = amount - p 
print("The Simple Interest is :", si)
print("The Compound Interest is :", ci)
