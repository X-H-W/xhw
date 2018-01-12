def app(name,newname):
	full = name + newname
	return full
a = app('你','好')
print(a)
'''
def app(first_name,last_name):
	full = first_name + last_name
	return full.title()
while True:
	print('\nPlease tell me your name:')
	f = input('输入')
	if f == 'f':
		print('66')
		break
	q = input('不熟')
	if q == 'q':
		print('no')
		break
c = app('hello','hi')
print('\nHello,' + c + '!')
'''

def make_album():
	a = {'小新':'蜡笔'}
	c = {'喜洋洋':'灰太浪'}
	print(a,c)
b = make_album()

