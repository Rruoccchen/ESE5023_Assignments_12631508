def print_values(): #define the function print_values
    a = int(input("please enter a = "))# ask user to input a value for a，b,c
    b = int(input("please enter b = "))
    c = int(input("please enter c = "))
    if a > b: #if a is greater than b, then check if b is greater than c
        if b > c: 
            print("a","b","c")
        elif a > c:
            print("a","c","b")
        else:
            print("c","a","b")
    elif b > a:
        if b < c: #this is opposite of b > c
            print("c","b","a")

print_values() # call the function print_values