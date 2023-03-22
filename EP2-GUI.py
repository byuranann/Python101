from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('แบบฟอร์มสมัครเรียน Python 101')
GUI.geometry('500x400')
#
l1 = Label(GUI,text='แบบฟอร์มสมัครเรียน Python 101',font=('Angsana New',30),fg='blue')
l1.place(x=55,y=20)

l2 = Label(GUI,text='ชื่อ',font=('Angsana New',30),fg='blue')
l2.place(x=50,y=100)
l3 = Label(GUI,text='นามสกุล',font=('Angsana New',30),fg='blue')
l3.place(x=50,y=150)
#
box1 = Entry(GUI)
box2 = Entry(GUI)

box1.place(x=200, y=120)
box2.place(x=200, y=170)
#

def Button2():
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('ยืนยันการสมัคร',text)

fb1 = Frame(GUI)
fb1.place(x=200,y=300)
b2 = ttk.Button(fb1,text='บันทึก', command=Button2)
b2.pack(ipadx = 20,ipady = 20)


GUI.mainloop()
