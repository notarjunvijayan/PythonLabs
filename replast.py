lst1 = [1,2,3,4,5]
lst2 = []
len = int(input("Enter the length of list: "))
for i in range(len):
    val = input("Enter value to inserted: ")
    datype = int(input("Enter 1 if sring and 2 if integer:"))
    if datype == 1:
        lst2.append(val)
    elif datype == 2:
        lst2.append(int(val))

lst1[4] = lst2
print("First List now replaced to: {}".format(lst1))