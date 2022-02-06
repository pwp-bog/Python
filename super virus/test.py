import os
import random

a = input()

ran_num = random.randint(1, 5)
if ran_num == 3:
    #os.system('shutdown -s')
    print("Lucky")
    os.chdir("C:\Folder")
    text_file = open("text.txt", "w")


