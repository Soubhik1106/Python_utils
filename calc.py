from tkinter import *


root = Tk()
root.title("Calculator")
root.iconbitmap("D:\Programs\c++_with_vscode\Python_with_VScode\calc.ico")

e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


#num click function
def button_click(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

#clear function
def button_clear():
    e.delete(0,END)


#add function
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)

#equal to function
def button_equal():
    second_number=e.get()
    e.delete(0,END)

    if math=="addition":
         e.insert(0, f_num +int (second_number))

   

    if math=="subtraction":
         e.insert(0, f_num -int (second_number))
    

    if math=="multiplication":
         e.insert(0, f_num * int (second_number))

    if math=="division":
         e.insert(0, f_num /int (second_number))

    


    


#subtraction funtion
def button_sub():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)


#product function
def button_mult():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)


#division function
def button_div():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)






#Declaring buttons
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))

button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_clr=Button(root,text="Clr",padx=20,pady=20,command=lambda:button_clear())
button_add=Button(root,text="+",padx=40,pady=20,command=button_add)
button_equal=Button(root,text="=",padx=40,pady=20,command=button_equal)

button_sub=Button(root,text="-",padx=40,pady=20,command=button_sub)
button_mult=Button(root,text="x",padx=40,pady=20,command=button_mult)
button_div=Button(root,text="/",padx=40,pady=20,command=button_div)


#showing buttons

button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)

button_4.grid(row=4 ,column=0)
button_5.grid(row=4 ,column=1)
button_6.grid(row= 4,column=2)

button_7.grid(row=5 ,column=0)
button_8.grid(row= 5,column=1)
button_9.grid(row= 5,column=2)
button_0.grid(row=6,column=0)

button_clr.grid(row=6,column=5,columnspan=2)
button_add.grid(row=6,column=1,columnspan=1)
button_equal.grid(row=6,column=2)

button_div.grid(row=7,column=0)
button_mult.grid(row=7,column=1)
button_sub.grid(row=7,column=2)


#the main loop
root.mainloop()