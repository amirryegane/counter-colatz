number = int(input("enter a number : "))

def Prime(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

if number%2==1:
    print("number is odd")
elif number<2:
    print("most be bigger than 2 ")
else:
    for i in range(number):
        if Prime(i) == 1:
            for l in range(i , number):
                if Prime(l) == 1:
                    if number == (i+l):
                        print(i , "+" , l ,"=" , number)