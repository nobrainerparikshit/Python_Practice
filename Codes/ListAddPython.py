a = input("Enter elements of list A separated by spaces: ").split()
b = input("Enter elements of list B separated by spaces: ").split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
length = len(a)
if len(b) > length:
    length = len(b)
result = []
for i in range(length):
    if i < len(a):
        va = a[i]
    else:
        va = 0
    if i < len(b):
        vb = b[i]
    else:
        vb = 0
    result.append(va + vb)
print("Element-wise sum:", result)
