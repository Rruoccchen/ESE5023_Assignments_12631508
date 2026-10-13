def Find_expression(target, start=0, total=0, expr=""): #this line is to define the function and set some parameters that will used in this function
    a = "123456789" # this is the string input "123456789"

    if start == len(a):
        if total == target:
            print(expr + "=" + str(target))
        return

    for end in range(start + 1, len(a) + 1):
        part = a[start:end]
        num = int(part)
        if start == 0:
            Find_expression(target, end, num, part)
        else:
            Find_expression(target, end, total + num, expr + "+" + part)
            Find_expression(target, end, total - num, expr + "-" + part)

Find_expression(50)
