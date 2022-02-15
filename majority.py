# Program to find out majority element in a list
def fredict(lis):
    dic = {}
    for element in lis:
        if not element in lis:
            dic[element] = 1
        else:
            dic[element] += 1
    return dic


leng = int(input("Enter the elements in the list: "))
lst = []
fre = {}
for i in range(leng):
    ele = input(f"Enter element {i}: ")
    lst.append(ele)
fre = fredict(lst)
print(fre)

