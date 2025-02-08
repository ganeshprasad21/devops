from functools import reduce
x = int(input("enter x : "))
y = lambda x: x * x * x * x
pow_4 = y(x)
print(f" value of (x) ^ 4  is {pow_4}")

l = [1,2,3,4,5,6,7]

print([*map(lambda x: x*x, l)],[*filter(lambda x: x%2 == 0,l)], reduce(lambda x,y: x+y,l))