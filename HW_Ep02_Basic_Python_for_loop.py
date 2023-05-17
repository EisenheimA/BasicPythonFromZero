import turtle

tao=turtle.Pen() #1 คำอธิบายอยู่ด้านล่าง
turtle.bgcolor('black') #2
tao.shape('turtle') #3
tao.pen(pencolor='white', pensize=9, speed=1000) #4
color=['gray','indigo','turquoise','yellow','orange','brown','red'] #5

def Home(): #6
    tao.penup()
    tao.home()
   
def SpirographA(): #7A
    for i in range (4): #8
        tao.penup()
        tao.goto((i*150)-250,0)
        tao.pendown()
        for i in range(100): #9
            tao.pencolor(color[i%7]) #10
            tao.width(i//200) #11
            tao.fd(i*0.5) #12
            tao.rt(50) #13
        tao.fd(i/5) #14
        Home() #15

def SpirographB(): #7B
    for i in range (4): #8
        tao.penup()
        tao.goto((i*150)-250,150)
        tao.pendown()
        for i in range(100): #9
            tao.pencolor(color[i%7]) #10
            tao.width(i//200) #11
            tao.fd(i*0.5) #12
            tao.rt(50) #13
        tao.fd(i/5) #14

SpirographA() #มี function Home()
SpirographB() #ไม่มี function Home()
Home()

'''
#1 = เพิ่มความสามารถในการใช้ปากกา
#2 = เปลี่ยนสีพื้นหลัง
#3 = เปลี่ยนรูปปากกาเป็น Square/Arrow/Circle/Turtle/Triangle/Classic ได้
#4 = เปลี่ยนสีปากกา/ขนาดปากกา/ความเร็วปากกา
#5 = สร้าง list ตัวแปรค่าสี
#6 = function คำสั่งให้ปากกากลับไปอยู่ที่ตำแหน่ง (0,0) และอยู่ในทิศเริ่มต้น
#7 = function คำสั่งให้ปากกาเคลื่อนที่ (A)มีFn Home (B)ไม่มีFn Home
#8 = คำสั่ง for loop หลัก (ใน loop นี้ให้ทำงาน 4 รอบ)
#9 = คำสั่ง for loop รอง (ใน loop นี้ให้วาดเส้น 100 เส้น)
#10 = เปลี่ยนสีปากกา โดยใช้ค่า(เฉพาะเศษ)ที่ได้จากการหาร i ด้วย 7
#11 = เปลี่ยนความกว้างปากกา เลือกค่า(เฉพาะเลขจำนวนเต็ม)ที่ได้จากการหาร i ด้วย 200 โดยที่ปัดเศษทิ้ง
#12 = สั่งให้ปากกาเคลื่อนที่เท่ากับ i*0.5 หน่วย
#13 = เลี้ยวขวามุม 50 องศา
#14 = สั่งให้ปากกาเคลื่่อนที่เพิ่มเพื่อเก็บปลายเส้น
#15 = หากไม่สั่ง Home รูปที่ได้ทั้งหมดไม่เหมือนกัน เพราะเริ่มต้นด้วยองศาที่ต่างกัน
'''
