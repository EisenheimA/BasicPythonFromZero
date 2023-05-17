# GUI_calc_unclefarm.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณสินค้าในฟาร์ม')
GUI.geometry('500x550')

bg = PhotoImage(file = 'unclefarm.png')
BG = Label(GUI, image = bg)
BG.pack()

durian_pic=PhotoImage(file='pic_durian.png')
lemon_pic=PhotoImage(file='pic_lemon.png')
mango_pic=PhotoImage(file='pic_mango.png')

Label = Label(GUI, text = "กรุณาระบุน้ำหนัก (กิโลกรัม)", font = (None, 20))
Label.pack()

v_quan = StringVar()
E1 = ttk.Entry(GUI, textvariable = v_quan, font =(None, 20))
E1.pack()

def Calc1():
	try:
		quantity = float(v_quan.get())
		calc = quantity * 159
		messagebox.showinfo('ราคาทั้งหมด', 'ราคาทุเรียนทั้งหมด {} บาท'.format(calc))
		v_quan.set(' ')
		E1.focus()
	except:
		messagebox.showwarning('กรอกข้อมูลผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quan.set('1')
		E1.focus()

def Calc2():
	try:
		quantity = float(v_quan.get())
		calc = quantity * 79
		messagebox.showinfo('ราคาทั้งหมด', 'ราคาเลมอนทั้งหมด {} บาท'.format(calc))
		v_quan.set(' ')
		E1.focus()
	except:
		messagebox.showwarning('กรอกข้อมูลผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quan.set('1')
		E1.focus()

def Calc3():
	try:
		quantity = float(v_quan.get())
		calc = quantity * 59
		messagebox.showinfo('ราคาทั้งหมด', 'ราคามะม่วงทั้งหมด {} บาท'.format(calc))
		v_quan.set(' ')
		E1.focus()
	except:
		messagebox.showwarning('กรอกข้อมูลผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quan.set('1')
		E1.focus()

B1 = ttk.Button(GUI,image=durian_pic,command=Calc1)
B1.pack(ipadx=30,ipady=5,pady=20)
B2 = ttk.Button(GUI,image=lemon_pic,command=Calc2)
B2.pack(ipadx=30,ipady=5)
B3 = ttk.Button(GUI,image=mango_pic,command=Calc3)
B3.pack(ipadx=30,ipady=5,pady=20)

GUI.mainloop() # for back at 1st line of program

