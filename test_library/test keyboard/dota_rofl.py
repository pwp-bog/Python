import keyboard
import time
import random

for i in range(2):
    print(f"До запуска осталось {i+1} секунд...")
    time.sleep(1)

# time.sleep(0.3)
# keyboard.send("win")
# time.sleep(0.3)
# keyboard.write("Блокнот")
# time.sleep(0.3)
# keyboard.send("enter")

keyboard.send("F9")


value_list = ["удаляй доту бездарь", "отъебал тебя, выехал к твоей маме",
              "zxc kaneki ghoul", "????", "я на калбасе вапросы????", "суетааа....", "кто твой папочка???", "Чо с ебалом???", "1000-7"]
value = random.choice(value_list)
num = 1000

for i in range(15):
    if value == "1000-7":
        time.sleep(0.09)
        keyboard.send("shift + enter")
        time.sleep(0.09)
        keyboard.write(f"{num} - 7 = {num-7}")
        num-=7
        time.sleep(0.09)
        keyboard.send("enter")
        time.sleep(0.09)
    else:
        time.sleep(0.09)
        keyboard.send("shift + enter")
        time.sleep(0.09)
        keyboard.write(value)
        time.sleep(0.09)
        keyboard.send("enter")
        time.sleep(0.09)
    # keyboard.write(value)
    # keyboard.send("enter")

keyboard.send("F9")
