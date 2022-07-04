t=int(input())
while t>0:
    t-=1
    a=input()
    b=0
    for x in a:
        if (x=="4") or (x=="7"):
            b+=1

    if (b==4) or (b==7):
        print("YES")
    else:
        print("NO")