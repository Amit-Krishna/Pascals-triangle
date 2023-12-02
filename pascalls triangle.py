from math import factorial as fact
a= int(input("num "))
for i in range(a):
    for j in range(i+1):
        print(int(fact(i)/(fact(j)*fact(i-j))), end="")
    print("")
