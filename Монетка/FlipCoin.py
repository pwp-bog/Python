import random
list = ["Орёл", "Решка"]
while(True):
	inputZnach = input('Выберите Орёл или Решка и введите данное значение в консоль: ')
	randomZnach = random.choice(list)
	if (randomZnach == inputZnach):
		print('Вы угадали, поздравляю')
	else:
		print('Попробуйте ещё...')
		print("В следующий раз получится)")

