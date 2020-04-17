import string
cloumn_row = input("Input the column and row (without spaces): ")
column = str(cloumn_row[0])
row = int(cloumn_row[1])
a = string.ascii_lowercase
for i in range(len(a)):
    if a[i - 1] == column:
        column = i
if column % 2 == 0:
    if row % 2 == 0:
        print("Black")
    else:
        print("White")

else:
    if row % 2 == 0:
        print("White")
    else:
        print("Black")