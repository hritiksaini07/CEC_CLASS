n=int(input())
for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i*2+1):
        print("*",end=" ")
    print("")