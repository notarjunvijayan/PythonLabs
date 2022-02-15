flag = 0
num = int(input("Enter the number: "))
while num >= 2:
    if num == 2:
        flag = 0
        print("Given number is a power of 2")
    else:
        flag = 1
    num = num / 2
if flag == 1:
    print("Given number is not a power of 2: ")
