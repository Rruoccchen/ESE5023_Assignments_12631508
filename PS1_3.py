def Pascal_triangle(x):
    row = [1]
    for line in range(1, x):
        new_row = [1]
        k = len(row) - 1
        for i in range(k):
            left_number = row[i]
            right_number = row[i + 1]
            middle_number = left_number + right_number
            new_row.append(middle_number)

        new_row.append(1)
        row = new_row
    print(row)

Pascal_triangle(100)
Pascal_triangle(200)