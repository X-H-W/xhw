row = 1
while row <= 9:
    col = 1
    while col+1 <= row:
        print('%d*%d=%d'%(col,row,col*row),end='/t')
        col += 1 
    print('%d*%d=%d'%(row,col,row*col))
    row += 1
'''
for i in range(1,10):
    for o in range(1,i+1):
        print('%d*%d=%d'%(i,o,i*o),end='\t')
    print('\t')
'''
