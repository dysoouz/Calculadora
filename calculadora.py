from tkinter import *





#Cores
gray = "#454440"
white_gray = "#8b9394"
white = "#edf1f5"
blue = "#1d3452"
orange = "#db9514"

#window
window = Tk()
window.title("CALCULADORA")
window.geometry("330x320")
window.config(bg=gray)

#frames
panel_frame = Frame(window,width=320,height=50,bg=blue)
panel_frame.grid(column=0,row=0,padx=5)

panel_body = Frame(window,width=335,height=270)
panel_body.grid(column=0,row=1,padx=5,pady=5)

#Calculation
def calculation(event):
    result = eval(event)
    result_text.set(result)

value_label = ''
def input_value(event):
    global value_label
    value_label = value_label + str(event)

    #passing value to label
    result_text.set(value_label)

def off_label():
    global value_label
    value_label = ''
    result_text.set(value_label)


result_text = StringVar()
#Label
cal = Label(panel_frame,textvariable=result_text,height=1,width=20,bg=blue,relief=FLAT, font=('Ivy 13 bold'), anchor='e',justify=RIGHT)
cal.place(x=90,y=10)

#Buttons
b_c = Button(panel_body,command= lambda: off_label(), text="C", width=13, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_c.grid(column=0,row=0,columnspan=2)
b_por = Button(panel_body,command= lambda: input_value('%'), text="%", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_por.grid(column=2,row=0)
b_div = Button(panel_body,command= lambda: input_value('/'), text="/", width=10, height=2, bg=orange, fg=white, font=('Ivy 13 bold'))
b_div.grid(column=3,row=0)

b_7 = Button(panel_body,command= lambda: input_value('7'), text="7", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_7.grid(column=0,row=1)
b_8 = Button(panel_body,command= lambda: input_value('8'), text="8", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_8.grid(column=1,row=1)
b_9 = Button(panel_body,command= lambda: input_value('9'), text="9", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_9.grid(column=2,row=1)
b_mul = Button(panel_body,command= lambda: input_value('*'), text="x", width=10, height=2, bg=orange, fg=white, font=('Ivy 13 bold'))
b_mul.grid(column=3,row=1)

b_4 = Button(panel_body,command= lambda: input_value('4'), text="4", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_4.grid(column=0,row=2)
b_5 = Button(panel_body,command= lambda: input_value('5'), text="5", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_5.grid(column=1,row=2)
b_6 = Button(panel_body, command= lambda: input_value('6'),text="6", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_6.grid(column=2,row=2)
b_sub = Button(panel_body, command= lambda: input_value('-'),text="_", width=10, height=2, bg=orange, fg=white, font=('Ivy 13 bold'))
b_sub.grid(column=3,row=2)

b_1 = Button(panel_body, command= lambda: input_value('1'),text="1", font=('Ivy 13 bold'), width=6, height=2, bg=white_gray, fg=white)
b_1.grid(column=0,row=3)
b_2 = Button(panel_body, command= lambda: input_value('2'),text="2", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_2.grid(column=1,row=3)
b_3 = Button(panel_body, command= lambda: input_value('3'),text="3", width=6, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_3.grid(column=2,row=3)
b_add = Button(panel_body, command= lambda: input_value('+'),text="+", width=10, height=2, bg=orange, fg=white, font=('Ivy 13 bold'))
b_add.grid(column=3,row=3)

b_0 = Button(panel_body, command= lambda: input_value('0'),text="0", width=20, height=2, bg=white_gray, fg=white, font=('Ivy 13 bold'))
b_0.grid(column=0,row=4,columnspan=3)

b_equal = Button(panel_body, command= lambda: calculation(result_text.get()),text="=", width=10, height=2, bg=orange, fg=white, font=('Ivy 13 bold'))
b_equal.grid(column=3,row=4)

window.mainloop()


