n = int(input("enter ur number : "))
m = 0
while n>1:
    if (n%2==0):
        n=n/2
    else:
        n = n*3+1
    m +=1
    print(m ,n )