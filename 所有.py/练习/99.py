row = 1
while row <= 9:
    col = 1
    while col+1 <= row:
        print("%d*%d=%d"%(row,col,row*col),end="\t")
        col += 1
    print("%d*%d=%d"%(row,col,row*col))
    row += 1
