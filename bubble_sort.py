def bubble_sort(l,n):
    for i in range(n):
        for j in range(n-i):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]

l=[int(l) for l in input().split()]
n=len(l)
bubble_sort(l,n)
print(l)