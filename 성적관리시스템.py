from tkinter import *

name = []
score = []

def click1():  #�߰� ��ư �Լ� �����κ� 
    display.insert(END,"123")


window = Tk()

lbl = Label(window, text="�̸�  ")
lbl.grid(row=0, column=0)

top_row = Frame(window)
top_row.grid(row=0,column=1,columnspan=2,sticky=N)
display=Entry(top_row,width=30,bg="light green")
display.grid()

lbl2 = Label(window, text="    ����: ")
lbl2.grid(row=0, column=6)

top_row = Frame(window)
top_row.grid(row=0,column=7,columnspan=2,sticky=N)
display=Entry(top_row,width=20,bg="light green")
display.grid()

lbl3 = Label(window, text="          ")
lbl3.grid(row=0, column=15)

btn = Button(window, text="�߰�", width=5, command=click1)
btn.grid(row=0, column=40)

lbl3 = Label(window, text="    ��ȣ: ")
lbl3.grid(row=1, column=6)

top_row = Frame(window)
top_row.grid(row=1,column=7,columnspan=2,sticky=N)
display=Entry(top_row,width=20,bg="light green")
display.grid()

lbl3 = Label(window, text="          ")
lbl3.grid(row=1, column=15)

btn = Button(window, text="����", width=5)
btn.grid(row=1, column=40)

lbl3 = Label(window, text="  �����̸�: ")
lbl3.grid(row=2, column=6)

top_row = Frame(window)
top_row.grid(row=2,column=7,columnspan=2,sticky=E)
display=Entry(top_row,width=20,bg="light blue")
display.grid()

btn = Button(window, text="����", width=5)
btn.grid(row=2, column=40)

lbl3 = Label(window, text="  �����̸�: ")
lbl3.grid(row=3, column=6)

top_row = Frame(window)
top_row.grid(row=3,column=7,columnspan=2,sticky=E)
display=Entry(top_row,width=20,bg="light blue")
display.grid()

btn = Button(window, text="����", width=5)
btn.grid(row=3, column=40)

btn = Button(window, text="��ȣ��", width=10)
btn.grid(row=4, column=3)

btn = Button(window, text="�̸���", width=10)
btn.grid(row=4, column=4)

btn = Button(window, text="������������", width=10)
btn.grid(row=4, column=5)

btn = Button(window, text="������������", width=10)
btn.grid(row=4, column=6)


window.mainloop()