#Incorrect Logic

str = input("Enter a string: ")  
for i in range(len(str)):
    flag = 0 
    for j in range(i+1,len(str)):
        if str[i] == str[j]:
            flag += 1
            break
        else:
            continue
    if flag == 0:
        print(str[i])