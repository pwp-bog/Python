def xo(string):
    string_o = 0
    string_x = 0
    for i in string.upper():
        if i == "O":
            string_o += 1
        if i == "X":
            string_x += 1

    if string_o == string_x:
        return True
    else:
        return False

