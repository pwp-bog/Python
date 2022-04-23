import keyboard as board
from time import sleep


sleep(0.3)
board.send("win")

sleep(0.3)
board.write("dota", delay=0.01)

sleep(0.3)
board.send("Enter")

