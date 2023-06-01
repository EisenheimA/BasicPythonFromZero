#oopfleamarket2.py

class Merchant:
	def __init__(self,category,sell,gender):
		self.category = category # กับข้าว,สลัด,ผลไม้
		self.sell = sell # ผัดกะเพรา/ผัดกระเทียม, สลัดผัก/สลัดโรล, มะม่วง/มะเฟือง/มะยงชิด
		self.gender = gender
	def sawasdee(self):
		if self.gender == 'ชาย':
			tone = 'ครับ'
		else:
			tone = 'ค่ะ'
		print(f'สวัสดี{tone} รับอะไรดี{tone}?')
	def sale(self):
		if self.category == 'กับข้าว':
			call = 'กับข้าว ไหม?จ๊ะ กับข้าว'
		elif self.category == 'สลัด':
			call = 'ทานสลัดเพื่อสุขภาพไหม? จ๊ะ'
		else:
			call = 'ผลไม้ สด ใหม่ จากสวน ทางนี้เลยจร้า'
		print(call)
	def food(self):
		if self.category == 'กับข้าว':
			price = '40 บาท'
			print(f'ถุงละ {price}บาท รับ{self.sell}เท่าไรดี? ค่ะ')
		elif self.category == 'สลัด':
			price = '35 บาท'
			print(f'กล่องละ {price}บาท รับ{self.sell}กี่กล่องดี? จ๊ะ')
		else:
			if self.sell == 'มะม่วง':
				price = '39 บาท'
				print(f'กิโลละ {price}บาท รับ{self.sell}กี่กิโลดี? ครับ')
			elif self.sell == 'มะเฟือง':
				price = '25 บาท'
				print(f'กิโลละ {price}บาท รับ{self.sell}กี่กิโลดี? ครับ')
			else:
				price = '70 บาท'
				print(f'กิโลละ {price}บาท รับ{self.sell}กี่กิโลดี? ครับ')

class Discount(Merchant):
	def __init__(self,category,sell,gender,jamnuan):
		super().__init__(category,sell,gender)
		self.jamnuan = jamnuan
	def discountfood(self,jamnuan='3 ถุง'):
		if jamnuan == '1 ถุง' or jamnuan == '2 ถุง':
			print('รับ 4 ถุง เลยไหม? เดี๋ยวแถมให้อีก 1 ถุง จร้า')
		else:
			print('ซื้อ 4 ถุง แถมเลยอีก 1 ถุง จร้า')
	def discountsalad(self,jamnuan='3 กล่อง'):
		if jamnuan == '3 กล่อง':
			print('3 กล่อง 100 คละกันได้ จ้า')
		else:
			print('3 กล่อง 100 ไปเลยจ้า')
	def discountfruit(self,jamnuan):
		if jamnuan == '1 กิโล' or jamnuan == '2 กิโล':
			print('ลดไม่ได้เลยครับ')
		elif jamnuan == '3 กิโล':
			print('เดี๋ยวแถมให้ ครับ')
		else:
			print('เดี๋ยวแถมให้ ครับ')

class Customer:
	def __init__(self,category,buy,jamnuan):
		self.category = category
		self.buy = buy
		self.jamnuan = jamnuan
	def ask(self):
		if self.category == 'กับข้าว':
			if self.buy == 'ผัดกะเพรา':
				kabkho = 'ผัดกะเพรา'
			else:
				kabkho = 'ผัดกระเทียม'
			print(f'{kabkho} ขายถุงละเท่าไร?')
		elif self.category == 'สลัด':
			if self.buy == 'สลัดผัก':
				salad = 'สลัดผัก'
			else:
				salad = 'สลัดโรล'
			print(f'{salad} ขายกล่องละเท่าไร?')
		else:
			if self.buy == 'มะม่วง':
				fruit = 'มะม่วง'
			elif self.buy == 'มะเฟือง':
				fruit = 'มะเฟือง'
			else:
				fruit = 'มะยงชิด'
			print(f'{fruit} ขายอย่างไร?')
	def buyer(self):
		if self.buy == 'ผัดกะเพรา':
			print('เอา{}มา {}'.format(self.buy,self.jamnuan))
		elif self.buy == 'ผัดกระเทียม':
			print('เอา{}มา {}'.format(self.buy,self.jamnuan))
		elif self.buy == 'สลัดผลไม้':
			print('เอา{}มา {}'.format(self.buy,self.jamnuan))
		elif self.buy == 'สลัดโรล':
			print('เอา{}มา {}'.format(self.buy,self.jamnuan))
		elif self.buy == 'มะม่วง':
			print('เอา{}มา {}'.format(self.buy,self.jamnuan))
		elif self.buy == 'มะเฟือง':
			print('เอา{}มา {}'.format(self.buy,self.jamnuan))
		else:
			print('เอา{}มา {}'.format(self.buy,self.jamnuan))

class Bargain(Customer):
	def __init__(self,category,buy,jamnuan):
		super().__init__(category,buy,jamnuan)
	def bargaing(self):
		if self.buy == 'ผัดกะเพรา' or self.buy == 'ผัดกระเทียม':
			if self.jamnuan == '1 ถุง' or self.jamnuan == '2 ถุง':
				print(f'เอามา {self.jamnuan}')
			else:
				print(f'ถ้าเอา {self.jamnuan} ลดให้อีกได้ไหม?')
		elif self.buy == 'สลัดผลไม้' or self.buy == 'สลัดโรล':
			if self.jamnuan == '1 กล่อง' or self.jamnuan == '2 กล่อง':
				print(f'เอามา {self.jamnuan}')
			else:
				print(f'ถ้าเอา {self.jamnuan} ลดให้อีกได้ไหม?')
		else:
			if self.buy == 'มะม่วง':
				if self.jamnuan == '1 กิโล' or self.jamnuan == '2 กิโล':
					print(f'ขอ{self.buy} {self.jamnuan}')
				else:
					print(f'ขอ{self.buy} {self.jamnuan} แถมให้หน่อยนะ พ่อค้า')
			elif self.buy == 'มะเฟือง':
				if self.jamnuan == '1 กิโล' or self.jamnuan == '2 กิโล':
					print(f'ขอ{self.buy} {self.jamnuan}')
				else:
					print(f'ขอ{self.buy} {self.jamnuan} ลดให้หน่อยนะ พ่อค้า')
			else:
				if self.jamnuan == '1 กิโล' or self.jamnuan == '2 กิโล':
					print(f'ขอ{self.buy} {self.jamnuan}')
				else:
					print(f'ขอ{self.buy} {self.jamnuan} ลดให้อีกหน่อยนะ พ่อค้า')
	def bargainok(self):
		if self.buy == 'ผัดกะเพรา' or self.buy == 'ผัดกระเทียม':
			print(f'เอามา 4 แถม 1')
		elif self.buy == 'สลัดผลไม้' or self.buy == 'สลัดโรล':
			print(f'เอามา 3 กล่อง')
		else:
			print(f'เอามา {self.jamnuan}')

if __name__ == '__main__':
	merchant1_1 = Merchant('กับข้าว','ผัดกะเพรา','หญิง')
	merchant1_2 = Merchant('กับข้าว','ผัดกระเทียม','หญิง')
	merchant2_1 = Merchant('สลัด','สลัดผลไม้','หญิง')
	merchant2_2 = Merchant('สลัด','สลัดโรล','หญิง')
	merchant3_1 = Merchant('ผลไม้','มะม่วง','ชาย')
	merchant3_2 = Merchant('ผลไม้','มะเฟือง','ชาย')
	merchant3_3 = Merchant('ผลไม้','มะยงชิด','ชาย')

	merchant1_3 = Discount('กับข้าว','ผัดกะเพรา','หญิง','4 ถุง')
	merchant1_4 = Discount('กับข้าว','ผัดกระเทียม','หญิง','4 ถุง')
	merchant2_3 = Discount('สลัด','สลัดผลไม้','หญิง','3 กล่อง')
	merchant2_4 = Discount('สลัด','สลัดโรล','หญิง','3 กล่อง')
	merchant3_4 = Discount('ผลไม้','มะม่วง','ชาย','3 กิโล')
	merchant3_5 = Discount('ผลไม้','มะเฟือง','ชาย','3 กิโล')
	merchant3_6 = Discount('ผลไม้','มะยงชิด','ชาย','3 กิโล')
	
	customer1_1 = Customer('กับข้าว','ผัดกะเพรา','2 ถุง')
	customer1_11 = Bargain('กับข้าว','ผัดกระเทียม','3 ถุง')
	customer1_2 = Customer('สลัด','สลัดโรล','1 กล่อง')
	customer1_21 = Bargain('สลัด','สลัดผลไม้','3 กล่อง')
	customer1_3 = Customer('ผลไม้','มะม่วง','1 กิโล')
	customer1_31 = Bargain('ผลไม้','มะยงชิด','2 กิโล')
	customer1_32 = Bargain('ผลไม้','มะเฟือง','3 กิโล')

	print('-----ที่ตลาดนัดวัดลิงขบ-----')
	merchant1_1.sawasdee()
	merchant2_1.sawasdee()
	merchant3_1.sawasdee()
	print('----เดินไปที่แผงขายอาหาร----')
	merchant1_1.sale()
	customer1_1.ask()
	merchant1_1.food()
	customer1_1.buyer()
	customer1_11.bargaing()
	merchant1_4.discountfood()
	customer1_11.bargainok()
	print('----เดินไปที่แผงสลัดบาร์----')
	merchant2_2.sale()
	customer1_2.ask()
	merchant2_2.food()
	customer1_2.buyer()
	customer1_21.bargaing()
	merchant2_3.discountsalad()
	customer1_21.bargainok()
	print('----เดินไปที่แผงผลไม้----')
	merchant3_1.sale()
	customer1_3.ask()
	merchant3_1.food()
	customer1_3.buyer()
	customer1_31.ask()
	merchant3_3.food()
	customer1_31.bargaing()
	customer1_32.ask()
	merchant3_2.food()
	customer1_32.bargaing()
	merchant3_6.discountfruit('3 กิโล')

'''
cm = categorymarket = {'กับข้าว':{'ผัดกะเพรา':'40 บาท','ผัดกระเทียม':'40 บาท'},
						'สลัด':{'สลัดผลไม้':'35 บาท','สลัดโรล':'40 บาท'},
						'ผลไม้':{'มะม่วง':'39 บาท','มะเฟือง':'25 บาท','มะยงชิด':'70 บาท'}}
for c in cm.keys():
	print(c)
for c in cm.values():
	print(c)
for k,v in cm.items():
	print('key={},value={}'.format(k,v))
print(cm['กับข้าว']['ผัดกะเพรา']) # 40 บาท
print(cm['กับข้าว']['ผัดกระเทียม']) # 40 บาท
print(cm['สลัด']['สลัดผลไม้']) # 35 บาท
print(cm['สลัด']['สลัดโรล']) # 35 บาท
print(cm['ผลไม้']['มะม่วง']) # 39 บาท
print(cm['ผลไม้']['มะเฟือง']) # 25 บาท
print(cm['ผลไม้']['มะยงชิด']) # 70 บาท
for cm_category,cm_sell in cm.items():
	print(cm_category) # กับข้าว/สลัด/ผลไม้
	print(cm_sell)	# {'ผัดกะเพรา':'40 บาท','ผัดกระเทียม':'40 บาท'}
					# {'สลัดผลไม้':'35 บาท','สลัดโรล':'35 บาท'}
					# {'มะม่วง': '39 บาท','มะเฟือง':'25 บาท','มะยงชิด':'70 บาท'}
	for key,value in cm_sell.items():
		print(key)	# 'ผัดกะเพรา'/'ผัดกระเทียม'/'สลัดผลไม้'/'สลัดโรล'/'มะม่วง'/'มะเฟือง'/'มะยงชิด'
		print(value)# 40 บาท'/'40 บาท'/'35 บาท'/'35 บาท'/'39 บาท'/'25 บาท'/'70 บาท'
'''
