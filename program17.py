n=int(input())
for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    for l in range(j,0,-1):
        print(l,end=" ")
    print("")
for i in range(n):
    for k in range(i+2):
        print(" ",end=" ")
    for j in range((n-i-2)+1):
        print(j+1,end=" ")
    for l in range(j,0,-1):
        print(l,end=" ")
    print("")