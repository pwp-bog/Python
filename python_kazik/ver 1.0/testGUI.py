from tkinter import *
from random import *
from tkinter.font import names

#  Функционал python казика

def sum_balance():

    global SummStavkaInfo
    global balance
    sum_balance_info = input_sum_info.get()
    input_sum_button.destroy()
    input_sum_info.destroy()

    global SRandom
    SRandom = choice(foo)


    if(sum_balance_info > balance):
        text = "Ошибка сумма ставки не может превышать баланс, попробуйте снова... "
        lbl['text'] = text
    if(sum_balance_info <= balance):
        text = "Ставка принята"
        lbl['text'] = text



        global Messagelast
        MessageLast = Label(window, text="Ваш баланс до ставки: ",bg="gray20" ,fg="white", font=("Arial Bold", 16))
        MessageLast.place(x = 40, y = 45)


        global MessageLastLast
        MessageLastLast = Label(window, text="Ваш баланс: ",bg="gray20" ,fg="white", font=("Arial Bold", 16))
        MessageLastLast.place(x = 270, y = 45)
        MessageLastLast['text'] = balance



        MessageLast = Label(window, text="Ваш баланс после ставки: ",bg="gray20" ,fg="white", font=("Arial Bold", 16))
        MessageLast.place(x = 40, y = 80)

        #FIXME Дрисня
        balance -= sum_balance_info
        MessageLastLast = Label(window, text="Ваш баланс после ставки : ".format(balance),bg="gray20" ,fg="white", font=("Arial Bold", 16))
        MessageLastLast.place(x = 300, y = 80)

        if((SRandom % 2 == 0) and (WhyColorInfo == "red")):
            text = "Вы выйграли)"
            lbl['text'] = text
            sum_balance_info *= 2
            balance += sum_balance_info



        elif((SRandom % 2 != 0) and (WhyColorInfo == "black")):
            text = "Вы выйграли)"
            lbl['text'] = text
            sum_balance_info *= 2
            balance += sum_balance_info


        elif((SRandom == 36) and (WhyColorInfo == "green")):
            text = "Вы выйграли)"
            lbl['text'] = text
            sum_balance_info *= 14
            balance += sum_balance_info


        else:
            text = "Вы проиграли..."
            lbl['text'] = text


def RedColorInfo():
    global WhyColorInfo
    WhyColorInfo = "red"  #  Это переменная хранящая цвет
    global text
    text = "Введите сумму Идля ставки: "
    lbl['text'] = text
    RedColorButton.destroy()
    BlackColorButton.destroy()
    GreenColorButton.destroy()


    global input_sum_info
    input_sum_info = Entry(window)
    input_sum_info.place(x = 5, y = 50, height=30,width=200)
    input_sum_info.focus()


    global input_sum_button
    input_sum_button = Button(window, text="Потвердить", fg="white", bg="red4",command=sum_balance)
    input_sum_button.place(x = 225, y = 50, height=30, width=100)


def BlackColorInfo():
    global WhyColorInfo
    global text
    WhyColorInfo = "black"
    text = "Введите сумму для ставки: "
    lbl['text'] = text
    RedColorButton.destroy()
    BlackColorButton.destroy()
    GreenColorButton.destroy()


    global input_sum_info
    input_sum_info = Entry(window)
    input_sum_info.place(x = 5, y = 50, height=30,width=200)
    input_sum_info.focus()


    global input_sum_button
    input_sum_button = Button(window, text="Потвердить", fg="white", bg="red4",command=sum_balance)
    input_sum_button.place(x = 225, y = 50, height=30, width=100)


def GreenColorInfo():
    global WhyColorInfo
    WhyColorInfo = "green"  #  Это переменная хранящая цвет
    global text
    text = "Введите сумму для ставки: "
    lbl['text'] = text
    RedColorButton.destroy()
    BlackColorButton.destroy()
    GreenColorButton.destroy()


    global input_sum_info
    input_sum_info = Entry(window)
    input_sum_info.place(x = 5, y = 50, height=30,width=200)
    input_sum_info.focus()


    global input_sum_button
    input_sum_button = Button(window, text="Потвердить", fg="white", bg="red4",command=sum_balance)
    input_sum_button.place(x = 225, y = 50, height=30, width=100)


def inputINFO():
    global balance
    balance = InputInformation.get()
    global text
    text = "Выберите и нажимте на выбранный вами цвет"
    lbl['text'] = text #  Это переменная хранящая сумму ставки
    InputInformation.destroy()
    InputInfo.destroy()


    global RedColorButton
    RedColorButton = Button(window, text="Красный", fg="white", bg="red", command=RedColorInfo)
    RedColorButton.place(x = 50, y = 50, height=30, width=100)


    global BlackColorButton
    BlackColorButton = Button(window, text="Чёрный", fg="white", bg="black",command=BlackColorInfo)
    BlackColorButton.place(x = 250, y = 50, height=30, width=100)


    global GreenColorButton
    GreenColorButton = Button(window, text="Зелёный", fg="white", bg="green",command=GreenColorInfo)
    GreenColorButton.place(x = 450, y = 50, height=30, width=100)


#  Сам гуи
global foo
foo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
window = Tk()
window.title("Python казик)")
window.geometry('800x500')
window.configure(background='gray20')
lbl = Label(window, text="Введите значение баланса: ",bg="gray20" ,fg="white", font=("Arial Bold", 16))   # через запятую,
lbl.grid(column=0, row=0)



InputInformation = Entry(window)
InputInformation.place(x = 5, y = 50, height=30,width=200)
InputInformation.focus()

InputInfo = Button(window, text="Потвердить", fg="white", bg="red4",command=inputINFO)
InputInfo.place(x = 225, y = 50, height=30, width=100)





window.mainloop()
