msg = '欢迎来到召唤师峡谷!'
print(msg)
name = 'wangzherongyao'
print(name.title())
print(name.upper())
print(name.lower())
first_name = '小'
last_name = '新'
print('尊敬的召唤师:'+first_name+last_name,'欢迎来到召唤师峡谷')
print('欢迎来到召唤师峡谷')
print('\t欢迎来到召唤师峡谷')
print('\n欢迎来到召唤师峡谷')
msg1 = '努力有用的话还要天才干甚?'
print(msg1)
msg1 = msg1.strip()
print(msg1)
num = 2
msg2 = ('尊敬的召唤师，您在这局中的综合评分为第'+str(num)+'位!你就是个渣')
print(msg2)

heroes = ['孙悟空','妖姬','ez','机器人','盲僧']
print(heroes)
print(heroes[0])
print(heroes[1])

heroes1 = ['孙悟空','妖姬','ez','机器人','盲僧']
print(heroes1)
heroes1[0]= '瑞文'
print(heroes1)

heroes2 = ['孙悟空','妖姬','ez','机器人',]
print(heroes2)
heroes2.append('盲僧')
print(heroes2)

heroes3 = ['孙悟空','妖姬','ez','机器人','盲僧']
heroes3.insert(0,'瑞文')
print(heroes3)

heroes4 = ['孙悟空','妖姬','ez','机器人','盲僧']
print(heroes4)
del heroes4[0]
print(heroes4)

heroes5 = ['孙悟空','妖姬','ez','机器人','盲僧']
print(heroes5)
tail = heroes5.pop()
print(heroes5)
print(tail)

heroes6 = ['孙悟空','妖姬','ez','机器人','盲僧']
print(heroes6)
heroes6.remove('ez')
print(heroes6)

heroes7 = ['孙悟空','妖姬','ez','机器人','盲僧']
heroes.sort()
print(heroes7)

heroes8 = ['孙悟空','妖姬','ez','机器人','盲僧']
heroes.sort(reverse = True)
print(heroes8)

heroes9 = ['孙悟空','妖姬','ez','机器人','盲僧']
print(heroes9)
print(sorted(heroes9))
print(heroes9)

heroes10 = ['孙悟空','妖姬','ez','机器人','盲僧']
print(heroes10)
heroes10.reverse()
print(heroes10)

heroes11 = ['孙悟空','妖姬','ez','机器人','盲僧']
len(heroes11)

heroes12 = ['孙悟空','妖姬','ez','机器人','盲僧']
for a in heroes12:
    print('您的队伍中有此英雄:'+a)

heroes13 = ['孙悟空','妖姬','ez','机器人','盲僧']
for a in heroes13:
    print(a+'是一个优秀的英雄!'+'\n')

for b in range(1,5):
    print(b)

num4 = list(range(1,6))
print(num)

pingfangji = []
for shuzi in range(1,11):
    pingfang = shuzi**2
    pingfangji.append(pingfang)
print(pingfangji)
