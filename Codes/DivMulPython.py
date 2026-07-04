start, end = 1200, 2200
both = [x for x in range(start, end+1) if x % 35 == 0]
print("Numbers divisible by both 7 and 5 (i.e. by 35):")
print(both)
divby7 = [x for x in range(start, end+1) if x % 7 == 0]
print("\nNumbers divisible by 7:")
print(divby7)
multof5 = [x for x in range(start, end+1) if x % 5 == 0]
print("\nNumbers that are multiples of 5:")
print(multof5)
