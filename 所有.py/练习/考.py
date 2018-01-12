#99乘法表
for i in range(1,10):
    for o in range(1,i+1):
        print("%d+%d=%d"%(i,o,i*o),end='\t')
    print('\t')
