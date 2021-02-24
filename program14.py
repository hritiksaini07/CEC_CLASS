n=int(input())
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range((n-i-1)*2+1):
        print(j+1,end=" ")
    print("")