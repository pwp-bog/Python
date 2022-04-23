import keyboard as board
from time import sleep
from config import url

sleep(0.3)
board.send("win")

sleep(0.3)
board.write("edge", delay=0.01)

sleep(0.3)
board.send("Enter")

sleep(1)
board.write(url, delay=0.000000000000000000000000000000000000000000000000000001)

board.send("Enter")
