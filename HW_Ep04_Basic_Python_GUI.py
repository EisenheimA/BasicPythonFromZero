#GUI-mouse.py
from tkinter import * # Lib: TK Interface
from tkinter import ttk # theme of TK
import pyautogui as pg # ใช้ "pg" แทน pyautogui
import webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปุ่ม') # เปลี่ยนชื่อโปรแกรม
GUI.geometry('500x300') # กำหนดขนาดหน้าจอ Interactive

def Carlendar(): # function กดปุ่มแสดงปฏิทิน
    pg.click(1280,747)

def Windows(): # function กดปุ่ม Windows
    pg.click(25,747)

def Google(): # function เรียก WebBrowser "google"
    webbrowser.open('https://www.google.co.th/')

B1 = ttk.Button(GUI, text='Calendar',command=Carlendar)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI, text='Windows',command=Windows) 
B2.pack(ipadx=20, ipady=10, pady=20) # ขนาดปุ่ม x,y,เว้นช่องไฟ

B3 = ttk.Button(GUI, text='Google',command=Google)
B3.pack(ipadx=20, ipady=10, pady=20)

GUI.mainloop() # คำสั่งใช้ปิดคำสั่งโค้ด ทำหน้าที่แสดงผลลัพธ์การทำงานค้างไว้

