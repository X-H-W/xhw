def greet_user():
	'''显示简单的问候'''
	print('Hello!')
greet_user()

def greet_user(username):
	'''显示简单的问候'''
	print('Hello,'+username.title()+'!')
greet_user('jesse')

def describe_pet(animal_type,pet_name):
	'''显示宠物的信息'''
	print('\nI have a '+ animal_type + '.')
	print("My"+animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('heamster','herry')

def describe_pet(animal_type,pet_name):
	'''显示宠物的信息'''
	print('\nI have a '+ animal_type + '.')
	print("My"+animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('hamster','harry')	
describe_pet('dog','willie')

def describe_pet(animal_type, pet_name):
	'''显示宠物的信息'''
	print('\nI have a '+ animal_type + '.')
	print("My"+animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('harry','hamster')

def describe_pet(animal_type, pet_name):
	'''显示宠物的信息'''
	print('\nI have a '+ animal_type + '.')
	print("My"+animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(animal_type = 'hamester', pet_name='harry')


def describe_pet(pet_name,animal_type='dog'):
	'''显示宠物的信息'''
	print('\nI have a '+ animal_type + '.')
	print("My"+animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(pet_name='willie')

def get_formatted_name(first_name,last_name):
	'''返回整洁的姓名'''
	full_name = first_name + ' ' +last_name
	return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name(first_name,middle_name,last_name):
	'''返回整洁的姓名'''
	full_name = first_name + ' ' + middle_name + ''+last_name
	return full_name.title()
musician = get_formatted_name('john','lee','hoker')
print('musician')

def get_formatted_name(first_name, last_name, middle_name=''):
	"""返回整洁的姓名"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name 
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)
		    
def build_person(first_name,last_name):
	'''返回一个字典，其中包含有关于一个人的信息'''
	person = {'first':first_name,'last':last_name}
	return person
musicain = build_person('jimi','hendrix')
print(musicain)

def build_person(first_name,last_name,age=''):
	'''返回一个字典，其中包含有关一个人的信息'''
	person = {'first':first_name,'last':last_name}
	if age:
		person['age'] = age
	return person
musican = build_person('jimi','hendrix',age = 27)
print(musician)

def get_formatted_name(first_name,lasst_name):
	'''返回整洁的姓名'''
	full_name = first_name + ' ' + last_name
	return full_name.title()
while True:
	print('\nPlease tell me your name:')
	print("(enter 'q' at any time)")
	f_name = input('First name:')
	if f_name == 'q':
		break
	l_name = input('Last name:')
	if l_name == 'q':
	formatted_name = get_formatted_name(f_name,l_name)
	print('\nHello,'+ formatted_name + '!')
