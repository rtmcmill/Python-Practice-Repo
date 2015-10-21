import random

row1=[random.randint(0,9)]
row2=[random.randint(0,9), random.randint(0,9)]
row3=[random.randint(0,9), random.randint(0,9), random.randint(0,9)]
row4=[random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]



class pyramid:
	def __init__(self, row_1, row_2, row_3, row_4):
		self.row_1 = row_1
		self.row_2 = row_2
		self.row_3 = row_3
		self.row_4 = row_4
		total = 0

	def print_rows(self):
		print self.row_1
		print self.row_2
		print self.row_3
		print self.row_4

	def max_total(self):

		#First Choice is default
		numb_chose = list()
		numb_chose.append(self.row_1[0])
		total = self.row_1[0]


		#Choice from row_2
		if(self.row_2[0] >= self.row_2[1]):
			total += self.row_2[0]
			numb_chose.append(self.row_2[0])
		else:
			total += self.row_2[1]
			numb_chose.append(self.row_2[1])

		#Choice from row_3
		if(self.row_3[0] >= self.row_3[1]):
			if(self.row_3[0] >= self.row_3[2]):
				total += self.row_3[0]
				numb_chose.append(self.row_3[0])
			else:
				total += self.row_3[2]
				numb_chose.append(self.row_3[2])

		elif(self.row_3[1] >= self.row_3[2]):
			total += self.row_3[1]
			numb_chose.append(self.row_3[1])
		
		else:
			total += self.row_3[2]
			numb_chose.append(self.row_3[2])
		


		#Choice from row_4
		if(self.row_4[0] >= self.row_4[1]):
			if(self.row_4[0] >= self.row_4[2]):
				if(self.row_4[0] >= self.row_4[3]):
					total += self.row_4[0]
					numb_chose.append(self.row_4[0])
				else:
					total += self.row_4[3]
					numb_chose.append(self.row_4[3])
			else:
				total += self.row_4[2]
				numb_chose.append(self.row_4[2])

		elif(self.row_4[1] >= self.row_4[2]):
			if(self.row_4[1] >= self.row_4[3]):
				total += self.row_4[1]
				numb_chose.append(self.row_4[1])
			else:
				total += self.row_4[3]
				numb_chose.append(self.row_4[3])

		elif(self.row_4[2] >= self.row_4[3]):
			total += self.row_4[2]
			numb_chose.append(self.row_4[2])
		
		else:
			total += self.row_4[3]
			numb_chose.append(self.row_4[3])


		print "The total is",total,"and the numbers are:",numb_chose

		
pyramid1 = pyramid(row1,row2,row3,row4)
pyramid1.print_rows()

print "\n\n\n"

pyramid1.max_total()
