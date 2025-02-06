def my_func(x):
    print("this is my func, x= ", x)

x = int(input("enter x : "))

for i in range(x):
    my_func(i)