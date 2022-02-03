def reverse(num):
    str = ""
    for i in num:
        str = i + str
    return str

def sumpali(num):
    rev = reverse(num)
    if num == rev:
        print(num)
    else:
        intnum = int(num)
        intrev = int(rev)
        intnum += intrev
        num = str(intnum)
        sumpali(num)
    


num = input("Enter the number: ")
sumpali(num)