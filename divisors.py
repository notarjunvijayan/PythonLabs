def divisor(num):
    #Calculation
    evenum = 0
    evenlist = []
    oddlist = []
    oddnum = 0
    if num ==0:
        print("You have entered 0, dumbass")
    else:
        for i in range(1,num+1):
            if num%i == 0:
                if i%2 ==0:
                    evenum +=1
                    evenlist.append(i)
                else:
                    oddnum +=1
                    oddlist.append(i)
            else:
                continue
    #Output
    print("The Entered number is {}.".format(num))
    print("Number of Even Divisors: {}, {}".format(evenum,evenlist))
    print("Number of Odd Divisors: {}, {}".format(oddnum,oddlist))
    print("Total Divisors: {}".format(oddnum+evenum))

#Driver Function
num = int(input("Enter the number to check: "))
divisor(num)