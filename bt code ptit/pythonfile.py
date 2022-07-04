a = input()
a = a[::-1]
a = a.lower()
for x in a:
    if a[0] == 'y' and a[1] == 'p' and a[2] =='.':
        print("yes")
        break
    else:
        print("no")
        break