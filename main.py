from tkinter import *

root = Tk()
root.geometry("350x500")
root.title("Tic Tac Toe")
root.config(bg = "white")

startclicked = False
count = 0

def start():
  global startclicked
  button7["text"] = "X"
  startclicked = True

def reset():
  global startclicked, count
  button1["text"] = ""
  button2["text"] = ""
  button3["text"] = ""
  button4["text"] = ""
  button5["text"] = ""
  button6["text"] = ""
  button7["text"] = ""
  button8["text"] = ""
  button9["text"] = ""
  result.config(text= "")
  startclicked = False
  count = 0

var = ""

def unbeatable(button,value):
  global startclicked, count,var
  if button["text"] =="" and startclicked == True :
    button["text"] = "O"
    count = count+1
    if count ==1:
      if value ==8:
        middleadjacent1()
        var = "MA1"
        result.config(text=value)
      elif value ==4:
        middleadjacent2()
        var = "MA2"
        result.config(text=value)
      elif value ==9:
        corner1()
        var = "C1"
        result.config(text=value)
      elif value ==1:
        corner2()
        var = "C2"
        result.config(text=value)
      elif value ==6:
        middleaway1()
        var = "MAW1"
        result.config(text=value)
      elif value ==2:
        middleaway2()
        var = "MAW2"
        result.config(text=value)
    elif count >1:
      result.config(text=value)
      if var == "MA1":
        middleadjacent1()
      elif var =="MA2":
        middleadjacent2()
      elif var =="C1":
        corner1()
      elif var =="C2":
        corner2()
      elif var =="MAW1":
        middleaway1()
      elif var =="MAW2":
        middleaway2()
      
def middleadjacent1():
  if button8["text"] =="O" and button9["text"] !="X":
    button1["text"] = "X"
    if button4["text"] =="O":
      button3["text"] = "X"
      if button2["text"] =="O":
        button5["text"] = "X"
        result.config(text ="Better Luck Next Time")
      elif button5["text"] =="O" or button6["text"] =="O" or button9["text"] =="O":
        button2["text"] = "X"
        result.config(text ="Better Luck Next Time")
    else:
      x = [button2,button3,button5,button6,button9]
      for i in range(5):
        if x[i]["text"] =="O":
          button4["text"] = "X"
          result.config(text ="Better Luck Next Time")

def middleadjacent2():
  if button4["text"] =="O" and button1["text"] !="X":
    button9["text"] = "X"
    if button8["text"] =="O":
      button3["text"] = "X"
      if button6["text"] =="O":
        button5["text"] = "X"
        result.config(text ="Better Luck Next Time")
      elif button5["text"] =="O" or button2["text"] =="O" or button1["text"] =="O":
        button6["text"] = "X"
        result.config(text ="Better Luck Next Time")
    else:
      x = [button2,button3,button5,button6,button1]
      for i in range(5):
        if x[i]["text"] =="O":
          button8["text"] = "X"
          result.config(text ="Better Luck Next Time")

def corner1():
  if button9["text"] =="O":
    button1["text"] = "X"
    if button4["text"] =="O":
      button3["text"] = "X"
      if button2["text"] =="O":
        button5["text"] = "X"
        result.config(text ="Better Luck Next Time")
      elif button5["text"] =="O" or button6["text"] =="O" or button8["text"] =="O":
        button2["text"] = "X"
        result.config(text ="Better Luck Next Time")
    else:
      x = [button2,button3,button5,button6,button8]
      for i in range(5):
        if x[i]["text"] =="O":
          button4["text"] = "X"
          result.config(text ="Better Luck Next Time")

def corner2():
  if button1["text"] =="O":
    button9["text"] = "X"
    if button8["text"] =="O":
      button3["text"] = "X"
      if button6["text"] =="O":
        button5["text"] = "X"
        result.config(text ="Better Luck Next Time")
      elif button5["text"] =="O" or button2["text"] =="O" or button4["text"] =="O":
        button6["text"] = "X"
        result.config(text ="Better Luck Next Time")
    else:
      x = [button2,button3,button5,button6,button4]
      for i in range(5):
        if x[i]["text"] =="O":
          button8["text"] = "X"
          result.config(text ="Better Luck Next Time")

def middleaway1():
  if button6["text"] =="O" and button3["text"] !="X" and button2["text"] !="O":
    button9["text"] = "X"
    if button8["text"] =="O":
      button1["text"] = "X"
      if button4["text"] =="O":
        button5["text"] = "X"
        result.config(text ="Better Luck Next Time")
      elif button5["text"] =="O" or button2["text"] =="O" or button3["text"] =="O":
        button4["text"] = "X"
        result.config(text ="Better Luck Next Time")
    else:
      x = [button1,button2,button3,button4,button5]
      for i in range(5):
        if x[i]["text"] =="O":
          button8["text"] = "X"
          result.config(text ="Better Luck Next Time")
  
def middleaway2():
  if button2["text"] =="O":
    button1["text"] = "X"
    if button4["text"] =="O":
      button9["text"] = "X"
      if button8["text"] =="O":
        button5["text"] = "X"
        result.config(text ="Better Luck Next Time")
      elif button5["text"] =="O" or button3["text"] =="O" or button6["text"] =="O":
        button8["text"] = "X"
        result.config(text ="Better Luck Next Time")
    else:
      x = [button3,button5,button6,button8,button9]
      for i in range(5):
        if x[i]["text"] =="O":
          button4["text"] = "X"
          result.config(text ="Better Luck Next Time")

         
label1 = Label(root,text = "Tic Tac Toe", fg = "#66D6C9",bg = "white", font =("Arial", 15))
label1.place(x = 120, y = 30)

button1 = Button(root, bg = "#66D6C9", width = 5,  height =3,command = lambda: unbeatable(button1,1))
button1.place(x = 50, y = 100)

button2 = Button(root, bg = "#66D6C9", width = 5,  height =3,command = lambda: unbeatable(button2,2))
button2.place(x = 130, y = 100)

button3 = Button(root, bg = "#66D6C9", width = 5,  height =3,command = lambda: unbeatable(button3,3))
button3.place(x = 210, y = 100)

button4 = Button(root, bg = "#66D6C9", width = 5,  height =3,command = lambda: unbeatable(button4,4))
button4.place(x = 50, y = 170)

button5 = Button(root, bg = "#66D6C9", width = 5,  height =3,command = lambda: unbeatable(button5,5))
button5.place(x = 130, y = 170)

button6 = Button(root, bg = "#66D6C9", width = 5,  height =3,command = lambda: unbeatable(button6,6))
button6.place(x = 210, y = 170)

button7 = Button(root, bg = "#66D6C9", width = 5,  height =3,command = lambda: unbeatable(button7,7) )
button7.place(x = 50, y = 240)

button8 = Button(root, bg = "#66D6C9", width = 5,  height =3, command = lambda: unbeatable(button8,8))
button8.place(x = 130, y = 240)

button9 = Button(root, bg = "#66D6C9",  height =3, width = 5,command = lambda: unbeatable(button9,9))
button9.place(x = 210, y = 240)

start = Button(root, bg = "#66D6C9", text ="Start",width = 5, font =("Arial",12), command = start)
start.place(x = 130, y = 330)

reset = Button(root, bg = "#66D6C9", text ="Reset",width = 5, font =("Arial",12), command = reset)
reset.place(x = 130, y = 370)

result = Label(root,text = "" )
result.place(x = 100, y = 420)

root.mainloop()
