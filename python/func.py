def my_func(x):
    print("this is my func, x= ", x)

x = int(input("enter x : "))

for i in range(x):
    my_func(i)

def average(*num,**kwnum):
    sum = 0
    for n in num:
        sum += n
    print(type(num))
    print(sum/len(num))

average(1,2,3,4,5,6)