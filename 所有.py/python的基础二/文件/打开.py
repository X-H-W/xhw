#写
'''
f = open('test.txt','w')
f.write('你好')
f.write('不好')
f.close()
'''
#读

f = open('one.two','r')
content = f.read(5)
print(content)
content = f.read()
print('*'*30)
print(content)
f.close()
