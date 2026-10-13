x = int(input("Please type a number between 1 and 100: "))  #this is to ask the user to input a number between 1 and 100, and convert it to an integer
def least_moves(x):
    moves = 0 #this is to initialize the variable moves to 0, which will be used to count the number of moves needed to
    while x > 1: #since the initial value is 1 RMB, here should be greater than 1, because if it is equal to 1, then no moves are needed
        if x % 2 == 0: # this is to judge whether the value of x is even or odd, if it is even, then it can be divided by 2
            x = x / 2
            moves = moves + 1
        else:
            x = x - 1 #this is to subtract 1 from x, because if it is odd, then it cannot be divided by 2, so we need to subtract 1 to make it even
            moves = moves + 1 #this is to count the number of moves needed
    return moves

print(least_moves(x))



