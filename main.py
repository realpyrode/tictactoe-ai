from tkinter import *

root = Tk()
root.geometry("350x500")
root.title("Tic Tac Toe")
root.config(bg="#F8FFF4")

startclicked = False
count = 0
var = ''


def start():
    global startclicked
    button7['text'] = 'X'                 #always starts here
    startclicked = True


def reset(): #clear all buttons
    global startclicked, count
    button1['text'] = ""
    button2['text'] = ""
    button3['text'] = ""
    button4['text'] = ""
    button5['text'] = ""
    button6['text'] = ""
    button7['text'] = ""
    button8['text'] = ""
    button9['text'] = ""
    result['text'] = ""
    startclicked = False
    count = 0


def unbeatable(button, value):
    global startclicked, count, var
    if button['text'] == "" and startclicked == True:      #making sure user does not start
        button['text'] = 'O'
        count = count + 1
        if count == 1:
            if value == 8:                 #value sent by buttons
                middleadjacent8()
                var = '8'
            elif value == 4:
                middleadjacent4()
                var = '4'
            elif value == 1:
                corner1()
                var = '1'
            elif value == 9:
                corner9()
                var = '9'
            elif value == 2:
                middleaway2()
                var = '2'
            elif value == 6:
                middleaway6()
                var = '6'
            elif value == 5:
                button3['text'] = 'X'
                var = '5'
            elif value == 3:
                oppocorner()
                var = '3'

        elif count == 2:
            if var == '5':
                if value == 1:
                    center_corner()
                    var = '5_1'
                elif value == 9:
                    center_corner()
                    var = '5_9'
                elif value == 2:
                    center_middle2()
                    var = '5_2'
                elif value == 6:
                    center_middle6()
                    var = '5_6'
                elif value == 8:
                    center_middle8()
                    var = '5_8'
                elif value == 4:
                    center_middle4()
                    var = '5_4'
            else:
                if var == '8':
                    middleadjacent8()
                elif var == '4':
                    middleadjacent4()
                elif var == '1':
                    corner1()
                elif var == '9':
                    corner9()
                elif var == '2':
                    middleaway2()
                elif var == '6':
                    middleaway6()
                elif var == '3':
                    oppocorner()


        else:
            if var == '8':
                middleadjacent8()
            elif var == '4':
                middleadjacent4()
            elif var == '1':
                corner1()
            elif var == '9':
                corner9()
            elif var == '2':
                middleaway2()
            elif var == '6':
                middleaway6()
            elif var == '5_1':
                center_corner()
            elif var == '5_9':
                center_corner()
            elif var == '5_2':
                center_middle2()
            elif var == '5_4':
                center_middle4()
            elif var == '5_6':
                center_middle6()
            elif var == '5_8':
                center_middle8()
            elif var == '3':
                oppocorner()


def middleadjacent8():                   # function for deciding moves (if tree)
    if button8['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button3['text'] = 'X'
            if button2['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button6['text'] == 'O' or button9['text'] == 'O':
                button2['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button9]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def middleadjacent4():
    if button4['text'] == 'O':
        button9['text'] = 'X'
        if button8['text'] == 'O':
            button3['text'] = 'X'
            if button6['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button1['text'] == 'O' or button2['text'] == 'O':
                button6['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button1]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def corner9():
    if button9['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button3['text'] = 'X'
            if button2['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button6['text'] == 'O' or button8['text'] == 'O':
                button2['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button8]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def corner1():
    if button1['text'] == 'O':
        button9['text'] = 'X'
        if button8['text'] == 'O':
            button3['text'] = 'X'
            if button6['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button4['text'] == 'O' or button2['text'] == 'O':
                button6['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button3, button5, button6, button4]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def middleaway6():
    if button6['text'] == 'O':
        button9['text'] = 'X'
        if button8['text'] == 'O':
            button1['text'] = 'X'
            if button4['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button2['text'] == 'O' or button3['text'] == 'O':
                button4['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button1, button2, button3, button4, button5]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def middleaway2():
    if button2['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button9['text'] = 'X'
            if button8['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button5['text'] == 'O' or button3['text'] == 'O' or button6['text'] == 'O':
                button8['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button3, button5, button6, button8, button9]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')


def center_corner():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button1['text'] == 'O':
            button9['text'] = 'X'
            if button6['text'] == 'O':
                button8['text'] = 'X'
                result.config(text='Better Luck Next Time!')
            elif button8['text'] == 'O' or button2['text'] == 'O' or button4['text'] == 'O':
                button6['text'] = 'X'
                result.config(text='Better Luck Next Time!')
        else:
            if button9['text'] == 'O':
                button1['text'] = 'X'
                if button2['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
                elif button4['text'] == 'O' or button6['text'] == 'O' or button8['text'] == 'O':
                    button2['text'] = 'X'
                    result.config(text='Better Luck Next Time!')


def center_middle4():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button4['text'] == 'O':
            button6['text'] = 'X'
            if button9['text'] == 'O':
                button1['text'] = 'X'
                if button2['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text="Draw")
                elif button8['text'] == 'O':
                    button2['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button1['text'] == 'O' or button2['text'] == 'O' or button8['text'] == 'O':
                button9['text'] = 'X'
                result.config(text='Better Luck Next Time!')


def center_middle2():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button2['text'] == 'O':
            button8['text'] = 'X'
            if button9['text'] == 'O':
                button1['text'] = 'X'
                if button4['text'] == 'O':
                    button6['text'] = 'X'
                    result.config(text='Draw')
                elif button6['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button1['text'] == 'O' or button4['text'] == 'O' or button6['text'] == 'O':
                button9['text'] = 'X'
                result.config(text='Better Luck Next Time!')


def center_middle6():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button6['text'] == 'O':
            button4['text'] = 'X'
            if button1['text'] == 'O':
                button9['text'] = 'X'
                if button8['text'] == 'O':
                    button2['text'] = 'X'
                    result.config(text='Draw')
                elif button2['text'] == 'O':
                    button8['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button2['text'] == 'O' or button8['text'] == 'O' or button9['text'] == 'O':
                button1['text'] = 'X'
                result.config(text='Draw')


def center_middle8():
    if button5['text'] == 'O':
        button3['text'] = 'X'
        if button8['text'] == 'O':
            button2['text'] = 'X'
            if button1['text'] == 'O':
                button9['text'] = 'X'
                if button6['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Draw')
                elif button4['text'] == 'O':
                    button6['text'] = 'X'
                    result.config(text='Better Luck Next Time!')
            elif button4['text'] == 'O' or button6['text'] == 'O' or button9['text'] == 'O':
                button1['text'] = 'X'
                result.config(text='Better Luck Next Time!')


def oppocorner():
    if button3['text'] == 'O':
        button1['text'] = 'X'
        if button4['text'] == 'O':
            button9['text'] = 'X'
            if button5['text'] == 'O':
                button8['text'] = 'X'
                result.config(text='Better Luck Next Time')
            elif button8['text'] == 'O' or button2['text'] == 'O' or button6['text'] == 'O':
                button5['text'] = 'X'
                result.config(text='Better Luck Next Time')
        else:
            x = [button2, button8, button5, button6, button9]
            for i in range(5):
                if x[i]['text'] == 'O':
                    button4['text'] = 'X'
                    result.config(text='Better Luck Next Time')




#======================================================================================================================= buttons and GUI below
title_block = Label(root, text = "TicTacToe", font = ("Times", 25), bg = "#ffffff", fg = "#43B302")
title_block.pack(padx = 20, pady = 20)

buttonframe = Frame(root)
buttonframe.pack(padx = 20, pady = 20)


button1 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button1, 1))
button1.grid(row = 0, column = 0)

button2 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button2, 2))
button2.grid(row = 0, column = 1)

button3 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button3, 3))
button3.grid(row = 0, column = 2)

button4 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button4, 4))
button4.grid(row = 1, column = 0)

button5 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button5, 5))
button5.grid(row = 1, column = 1)

button6 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button6, 6))
button6.grid(row = 1, column = 2)

button7 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button7, 7))
button7.grid(row = 2, column = 0)

button8 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button8, 8))
button8.grid(row = 2, column = 1)

button9 = Button(buttonframe, text="", bg = "#b9ff9c", highlightcolor= "black", width = 5, height = 3, command = lambda: unbeatable(button9, 9))
button9.grid(row = 2, column = 2)

startbt = Button(root, text="Start", width = 5, height = 1, command = start, bg = "#b9ff9c")
startbt.pack(pady = 5, padx = 20)

resetbt = Button(root, text="Reset", width = 5, height = 1, command = reset, bg = "#b9ff9c")
resetbt.pack(pady = 10, padx = 20)

result = Label(root, text = "", font = ("Arial", 15), bg = "#F8FFF4")
result.pack()

root.mainloop()

