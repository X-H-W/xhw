age = int(input('请输入你的年龄'))

if age < 2:
    print('他是婴儿')
elif age >= 2 and age <= 4:
    print('庞珊学步')
elif age >= 4 and age <= 13:
    print('他是儿童，可以参加六一儿童节')
elif age >= 13 and age <= 20:
    print('他是青年人')
elif age >=20 and age <= 65:
    print('他是成年人')
