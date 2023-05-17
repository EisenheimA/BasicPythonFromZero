from tkinter import *
from tkinter import ttk, messagebox, PhotoImage
import math

GUI = Tk()
GUI.title('Angle of Twist')
GUI.geometry('900x500')

shear_modulus = {'Aluminium': 27.0,'Brass': 39.0,'Copper': 44.7,'Iron': 52.5,'Steel': 79.3,'Titanium': 41.4}

head = PhotoImage(file = 'pic_angletwist.png')
Head = Label(GUI, image = head)
Head.pack(side=RIGHT, padx=40)

L0 = Label(GUI,text='โปรแกรมคำนวณมุมของการบิด',font=(None,20))
L0.pack(side=TOP)

L1 = Label(GUI,text='ค่าความยาว A-B, L_AB (mm)',font=(None,10))
L1.pack()
ab_length = StringVar()
L_ab = ttk.Entry(GUI,textvariable=ab_length,font=(None,10))
L_ab.pack()

L2 = Label(GUI,text='ค่าความยาว B-C, L_BC (mm)',font=(None,10))
L2.pack()
bc_length = StringVar()
L_bc = ttk.Entry(GUI,textvariable=bc_length,font=(None,10))
L_bc.pack()

L3 = Label(GUI,text='ค่าความยาว B-C, L_BC (mm)',font=(None,10))
L3.pack()
cd_length = StringVar()
L_cd = ttk.Entry(GUI,textvariable=cd_length,font=(None,10))
L_cd.pack()

L4 = Label(GUI,text='ขนาดเส้นผ่าศูนย์กลาง, D1 (mm)',font=(None,10))
L4.pack()
d1_length = StringVar()
D1 = ttk.Entry(GUI,textvariable=d1_length,font=(None,10))
D1.pack()

L5 = Label(GUI,text='ขนาดเส้นผ่าศูนย์กลาง, D2 (mm)',font=(None,10))
L5.pack()
d2_length = StringVar()
D2 = ttk.Entry(GUI,textvariable=d2_length,font=(None,10))
D2.pack()

L6 = Label(GUI,text='ขนาดเส้นผ่าศูนย์กลาง, D3 (mm)',font=(None,10))
L6.pack()
d3_length = StringVar()
D3 = ttk.Entry(GUI,textvariable=d3_length,font=(None,10))
D3.pack()

L7 = Label(GUI,text='วัสดุAB: กรุณากรอกวัสดุที่มีเท่านั้น',font=(None,10))
L7.pack()
L8 = Label(GUI,text='Aluminium, Brass, Copper, Iron, Steel, Titanium',font=(None,8))
L8.pack()
m1_type = StringVar()
M1 = ttk.Entry(GUI,textvariable=m1_type,font=(None,10))
M1.pack()

L9 = Label(GUI,text='วัสดุBCD: กรุณากรอกวัสดุที่มีเท่านั้น',font=(None,10))
L9.pack()
L10 = Label(GUI,text='Aluminium, Brass, Copper, Iron, Steel, Titanium',font=(None,8))
L10.pack()
m2_type = StringVar()
M2 = ttk.Entry(GUI,textvariable=m2_type,font=(None,10))
M2.pack()

def Calc():
	a_b=float(ab_length.get())
	b_c=float(bc_length.get())
	c_d=float(cd_length.get())
	d_1=float(d1_length.get())
	d_2=float(d2_length.get())
	d_3=float(d3_length.get())
	m_1=str(m1_type.get())
	m_2=str(m2_type.get())

	if a_b and b_c and c_d and d_1 and d_2 and d_3 != 0:

		if m_1 in shear_modulus or m_1.title() in shear_modulus:
			G1 = (float(shear_modulus[m_1.title()]))*(10**9)
			angle1=(800*a_b*(10**-3)/((math.pi/2)*(((d_1/2)*(10**-3))**4)*(G1)))
		if m_2 in shear_modulus or m_2.title() in shear_modulus:
			G2 = (float(shear_modulus[m_2.title()]))*(10**9)
			angle2=(2400*b_c*(10**-3)/((math.pi/2)*(((d_2/2)*(10**-3))**4)*(G2)))
			angle3=(2400*b_c*(10**-3)/((math.pi/2)*((((d_2/2)*(10**-3))**4)-(((d_3/2)*(10**-3))**4))*(G2)))

			angle_twist = angle1+angle2+angle3

			messagebox.showinfo('Angle of Twist', 'มุมที่ถูกบิดไป {:f} radian'.format(angle_twist))
		else:
			messagebox.showwarning('ใส่ค่าไม่ถูกต้อง','กรุณากรอกเฉพาะวัสดุที่มีเท่านั้น')
	else:
		messagebox.showwarning('ใส่ค่าไม่ถูกต้อง','กรุณากรอกเฉพาะตัวเลขเท่านั้น')

B = ttk.Button(GUI, text='คำนวณ',command=Calc)
B.pack(ipadx=20,ipady=15,pady=20)

GUI.mainloop()