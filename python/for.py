for i in "ganesh prasad r":
    print(i)

print([x for x in "ganesh prasad r" if x != " "])

x = int(input("enter x: "))
while x > 1:
    if x == 6:
        x-=1
        continue
    if x == 200:
        break
    print(x)
    x -=1