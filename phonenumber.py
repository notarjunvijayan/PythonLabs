def missdigit(number):
    digits = []
    for i in range(10):
        if str(i) in num:
            continue
        else:
            digits.append(i)
    print(digits)

num = input("Enter the phone number: ")
if len(num) != 10:
    print("Invalid Length")
else:
    missdigit(num)