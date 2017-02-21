## create a 4x4 box using nested loops

def nested_box():

    box=""          ##initialize empty box
    row=4
    col=4
    char = '*'

    for i in range (row):       ## This defines the number of rows
        line=""
        for i in range (col):   # This defines the number of columns
            line=line+char
        line=line + "\n"        # line break after all elements in col returned
        box= box + line
    return box