

flag = False

while(flag == False):
    x = int(input("enter value for x: "))

    if x == 3:
        print("yay correct guess")
        flag = True
    elif x > 3: 
        print("ypu guessed somethimg higer")
    else:
        print("you guessed something lower")