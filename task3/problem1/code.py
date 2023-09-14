n=int(input("Enter limit: "))
def sum_odd():
    l=[]
    c=0
    for i in range(n):
        a=int(input())
        l.append(a)
    for j in l:
        if j%2!=0:
            c+=j
    print()
    print(c)
sum_odd()