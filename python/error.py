x=input("enter the valie of x: ")

try:
    if x % 3 == 0:
        print("divisible by 3")
except Exception as e:
    print("hi",e)