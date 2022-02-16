import win10toast

toast = win10toast.ToastNotifier()
test_data = input("Write you name: ")

if test_data == "Bogdan":
    toast.show_toast(title="PyScript", msg="Yes, i thing, this is very cool name", duration=5)
else:
    toast.show_toast(title="PyScript", msg="I think you should change your name", duration=5)