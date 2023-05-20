import requests
import bs4
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
import openpyxl

DATE = [] #13 วันที่ออกสลาก
LOTTO = [] #7 ประเภทรางวัล
HWY = [] #10 'หวย' หมายเลขรางวัล

for i in range(1,5):
	url = 'https://news.sanook.com/lotto/archive/page/{}/'.format(i)
	data = requests.get(url)

	web_data = bs4.BeautifulSoup(data.text,'html.parser') #1
	head_web = web_data.find_all('article',{'class':'archive--lotto'}) #2

	for h in head_web:
		#print(h.find('h3',{'class':'archive--lotto__head-lot'}).text) #3
		dates = (h.find('h3',{'class':'archive--lotto__head-lot'}).text) #3
		dates = dates.replace('ตรวจสลากกินแบ่งรัฐบาล ตรวจหวย','') #17
		#print(h.find_all('ul',{'class':'archive--lotto__result-list'})) #4
		result_lists = (h.find_all('ul',{'class':'archive--lotto__result-list'})) #4

		for rl in result_lists: #5
			for r in rl.find_all('em', {'class':'archive--lotto__result-txt'}): #6
				space1 = r.text
				space1 = space1.replace('ผลสลากกินแบ่งรัฐบาล','') #18
				if r.text == "ผลสลากกินแบ่งรัฐบาล รางวัลที่ 1": #19
					DATE.append(dates) #13
				else: #19
					DATE.append('-----')
				LOTTO.append(space1) #7
#print(len(LOTTO)) #8
		for rl in result_lists:
			for l in rl.find_all('strong',{'class':'archive--lotto__result-number'}): #9
				space2 = l.text
				space2 = space2.strip()
				space2 = space2.replace('\n',' ') #12
				HWY.append(space2) #10
#print(len(HWY)) #11
tables = pd.DataFrame([DATE,LOTTO,HWY]).transpose() #14
tables.columns = ['วันที่ออกสลาก','ประเภทรางวัล','หมายเลขรางวัล']
#print(tables)
tables.set_index('วันที่ออกสลาก',inplace=True) #16
tables.to_excel('data-lottery.xlsx',engine='openpyxl') #15
'''
#1 ดึงข้อมูล html ของ url มาจาก data.text สร้างเป็นตัวแปรชื่อ "web_data"
#2 ค้นหาข้อมูลเฉพาะ head ของ web จาก tag:'article'-class:'archive--lotto' แล้วสร้างเป็นตัวแปรชื่อ "head_web"
#3 ทำการกรอง tag:'h3'-class:'archive--lotto__head-lot' ได้ 'วันที่เดือนปี' ที่ออกสลาก >สร้างเป็นตัวแปรชื่อ "dates"
#4 ทำการกรอง tag:'ul'-class:'archive--lotto__result-list ได้ 'ประเภทรางวัล/หมายเลขรางวัล' >สร้างเป็นตัวแปรชื่อ "head_results"
#5 สร้างตัวแปร "rl" เป็น 'results_lists'
#6 ทำการกรอง tag:'em'-class:'archive--lotto__result-txt' ได้ 'ประเภทรางวัล'
#7 สร้าง list ชื่อ "LOTTO" ไว้เก็บค่า "ประเภทรางวัล" ที่ได้จาก #6 ใช้ *.append เพื่อเก็บค่า
#8 ทำการ print/len ข้อมูล ดูว่ามีข้อมูล/จำนวนข้อมูลที่เก็บไว้ใน list
#9 ทำการกรอง tag:'strong'-class:'archive--lotto__result-number' ได้ 'หมายเลขรางวัล'
#10 สร้าง list ชื่อ "HWY" ไว้เก็บค่า "หมายเลขรางวัล" ที่ได้จาก #9 ใช้ *.append เพื่อเก็บค่า เช่นกัน จะได้ ("\n"+"หมายเลขรางวัล") 
#11 ทำการ print/len ข้อมูล ดูว่ามีข้อมูล/จำนวนข้อมูลที่เก็บไว้ใน list เมื่อlenแล้ว จะต้องมีค่าเท่ากับ #8
#12 ทำการ replace เนื่องจาก strip แล้ว "\n" ไม่หมด
#13 สร้าง list ชื่อ "DATE" ไว้เก็บค่า "วันที่ออกสลาก" ที่ได้จาก #3
#14 สั่งให้ pandas สร้าง Frame และเปลี่ยน List จาก row ให้เป็น column
#15 สร้าง Excel ที่ชื่อ "data-lottery.xlsx"
#16 ตัด index ใน column แรกทิ้ง
#17 ตัดคำ "ตรวจสลากกินแบ่งรัฐบาล ตรวจหวย" ออก ให้เหลือเฉพาะวันที่
#18 ตัดคำ "ผลสลากกินแบ่งรัฐบาล" ออก ให้เหลือเฉพาะประเภทรางวัล
#19 สั่งให้ วันที่ออกสลาก ปรากฏเฉพาะ row ที่เป็น "รางวัลที่ 1" เท่านั้น นอกเหนือจากนั้น ให้เป็น '' (ช่องว่าง)
'''