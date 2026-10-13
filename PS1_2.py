#this is assignment 2.1
import random # because we will use the random module to generate a random number

M1 = []
for i in range(5):
     row1 = [] 
     for j in range(10): # this means that it will loop through the range of 10
        number = int(random.random() * 51)  #this will generate a random number between 0 and 50 and convert it to an integer
        row1.append(number)
     M1.append(row1)
print(M1) 

M2 = [] #same flow as M1, but with different dimensions     
for i in range(10):
     row2 = []
     for j in range(5):
        number = int(random.random() * 51)
        row2.append(number)
     M2.append(row2)
print(M2)

# the following is assignment 2.2
def matrix_multip(M1, M2):
    M3 = []
    for i in range(5): #this means to create a new list M3 with 5 rows
        row3 = []
        for j in range(5): #this means to create a new list row3 with 5 columns
            result = 0 #this means to initialize the variable result to 0, which will be used to store the sum of M1 and M2 elements
            for k in range(10): # it means this needs to be repeated 10 times, because M1 has 10 columns and M2 has 10 rows,
                result = result + M1[i][k] * M2[k][j] #this means to multiply the element in the ith row and kth column of M1 with the element in the kth row and jth column of M2, and add it to the result
            row3.append(result) #this is to append the result to the row3 list
        M3.append(row3) #this is to append the row3 list to the M3 list, which will create a new row in M3
    return M3 #this is to return the M3 list, which is the result of the matrix multiplication of M1 and M2

print(matrix_multip(M1, M2)) 
