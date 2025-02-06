x = int(input("enter value of x: "))

match x:
    case 0:
        print("u entered 0")
    case _ if x<10 :
        print("u entered some other than zero and less than 10")
    case _ if x>10:
        print("u entered something other than 0 >10")
    case _:
        print("corner case u entered 10")