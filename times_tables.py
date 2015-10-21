
print "This program prints the times tables"

col = 1
row = 1

while col < 11:
	while row < 11:
		print col*row,"\t",
		row += 1
	col += 1
	row = 1
	print "\n\r"

