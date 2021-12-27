string = input()
vowels = 0
consonants = 0
for i in range(0, len(string)):
    if string[i] in "ауоыиэяюёеАУОЫИЭЯЮЁЕ":
        vowels += 1
    if string[i] in "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
        consonants += 1

print("Количество гласных букв равно", vowels)
print("Количество согласных букв равно", consonants)
