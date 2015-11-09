##
# This program defines the hs procedure
#

def hs(n):
    print(n)
    counter = 1
    while n != 1 :
        counter = counter+1
        if n % 2 == 0 :
            n = n // 2
            print(n)
        else :
            n = 3*n+1
            print(n)

    print(counter)
