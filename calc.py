from tkinter import *
import parser




root=Tk()

display = Entry(root)

display.grid(row=1,columnspan=6)
def clear():
    display.delete(0,END)

i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i +=1
def undo():
    entire_string = display.get()
    if entire_string:
        new_string= entire_string[:-1]
        clear()
        display.insert(0,new_string)

def get_operation(x):
    global i
    lenth = len(x)
    display.insert(i,x)
    i += lenth

def calculator():
    entire_string= display.get()
    try:
        a= parser.expr(entire_string).compile()
        result=eval(a)
        clear()
        display.insert(0,result)
    except:
        clear()
        print("error")
def design(root):
    Button(root,text="0",command= lambda :get_variable('0')).grid(row=2,column=0)
    Button(root,text="1",command= lambda :get_variable('1')).grid(row=2,column=1)
    Button(root,text="2",command= lambda :get_variable('2')).grid(row=2,column=2)
    Button(root,text="3",command= lambda :get_variable('3')).grid(row=3,column=0)
    Button(root,text="4",command= lambda :get_variable('4')).grid(row=3,column=1)
    Button(root,text="5",command= lambda :get_variable('5')).grid(row=3,column=2)
    Button(root,text="6",command= lambda :get_variable('6')).grid(row=4,column=0)
    Button(root,text="7",command= lambda :get_variable('7')).grid(row=4,column=1)
    Button(root,text="8",command= lambda :get_variable('8')).grid(row=4,column=2)
    Button(root,text="9",command= lambda :get_variable('9')).grid(row=5,column=1)
    Button(root,text="+",command= lambda :get_operation('+')).grid(row=2,column=4)
    Button(root,text="-",command= lambda :get_operation('-')).grid(row=3,column=4)
    Button(root,text="*",command= lambda :get_operation('*')).grid(row=4,column=4)
    Button(root,text="/",command= lambda :get_operation('/ ')).grid(row=5,column=4)
    Button(root,text="->",command= lambda :undo()).grid(row=5,column=5)
    Button(root,text="ac",command= lambda :clear()).grid(row=5,column=0)
    Button(root,text="=",command= lambda :calculator()).grid(row=5,column=2)

design(root)
root.mainloop()