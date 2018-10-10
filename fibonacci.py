def fibonacci (aantal_getallen):
    x,y,temp = 0,1,0
    print(0)

    while (aantal_getallen > 0):
        temp = y; #vasthouden van de optelling
        y = y + x;  #wordt het volgende getal
        x = temp; #to print
        aantal_getallen=aantal_getallen-1
        print(x)
    return x


fibonacci(10)