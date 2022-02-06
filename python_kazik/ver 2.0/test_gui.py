from tkinter import *


def button_clicked():
    print(u"Клик!")


root = Tk()
# root["bg"] = "gray22"  # gray gray0-99
root.config(bg="gray22")
root.geometry("500x500")
root.title("Python казик")


label1 = Label(
    text="Введите сумму ставки:", fg="#eee", bg="#333",
    font=("Comic Sans MS", 24, "bold"))

label1.pack()


InputInformation = Entry(root)
InputInformation.place(x=150, y=150, height=30, width=200)
InputInformation.focus()

# кнопка с указанием родительского виджета и несколькими аргументами
button2 = Button(
    root, bg="green", text=u"Вывод сообщения в консоль", fg="white",
    command=button_clicked, height=5, width=500, font=("Comic Sans MS", 12, "bold"))

button2.pack(side=BOTTOM)
root.mainloop()
