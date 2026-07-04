name = input("Enter name: ")
age = int(input("Enter age: "))
basic = float(input("Enter basic salary: "))
da = 0.10 * basic
hra = 0.10 * basic
total_salary = basic + da + hra
print("Employee Name:", name)
print("Age:", age)
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("Total Salary:", total_salary)
