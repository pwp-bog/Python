import getpass
user = getpass.getuser()
password = getpass.getpass()

a = True
while a:
	if user != password:
		print("Неверный пароль")
		print("Попробуйте снова")
		password = getpass.getpass()
	else:
		print("Правильный пароль")
