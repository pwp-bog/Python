import keyboard as keyb
from time import sleep

sleep(0.3)
keyb.press("win")
keyb.release("win")


sleep(0.3)
keyb.write("Edge", delay=0.01)

sleep(0.3)
keyb.press("Enter")
keyb.release("Enter")

sleep(0.5)
keyb.write("www.vk.com", delay=0.01)

keyb.press("Enter")
keyb.release("Enter")

# Матвей должен меня слушаться!!!