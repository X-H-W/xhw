def modify(v):
    v[0] = v[0]+1
    return v 
a = [2]
print(modify(a))
print(a)

def modify2(v,item):
    v.append(item)
    return v
b = [4]
print(modify2(b,5))
print(b)
print('-'*30)

def modify3(c):
    c['age']=38
b = [4]
print(modify2(b,5))
print(b)
print('-'*30)

def modify3(c):
    c['age']=38
d = {'name':'宏伟','age':18}
print(d)
