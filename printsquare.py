#
def printSquare():
	n = 5
	flag = 0 #标记方向
	i_row, j_col = 0, -1
	
	# 产生 nXn 阶全0矩阵
	lstnum = [[0 for i in range(n)] for j in range(n)]

	num = 0
	# 之所以利用 while 循环是因为在最后一次转向后，如果没有回退，则会造成数字丢失，而回退只能用 while 来控制。
	while  num < n*n:
		num += 1		
		if flag%4 == 0: #向右
			j_col += 1
			if j_col<n and lstnum[i_row][j_col]==0 :
				lstnum[i_row][j_col] = num
			else:
				flag += 1
				j_col -= 1 #恢复到上一次
		if flag%4 == 1: #向下
			i_row += 1
			if i_row<n and lstnum[i_row][j_col]==0 :
				lstnum[i_row][j_col] = num
			else:
				flag += 1
				i_row -= 1
		if flag%4 == 2: #向左
			j_col -= 1				
			if j_col>=0 and lstnum[i_row][j_col]==0 :
				lstnum[i_row][j_col] = num
			else:
				flag += 1
				j_col += 1
		if flag%4 == 3: #向上			
			i_row -= 1
			if i_row>=0 and lstnum[i_row][j_col]==0 :
				lstnum[i_row][j_col] = num
			else:
				flag += 1
				i_row += 1
				num -= 1

	for item in lstnum:
		for ii in item:
			print("%4s" % ii, end="")
		print()
	# print(lstnum)

def genBirthday():
	lst1day = []
	lst2day = []
	lst3day = []
	lst4day = []
	lst5day = []
	for i in range(1, 32):
		tmp = str(bin(i))[2:].zfill(5)
		if tmp[4] == '1':
			lst1day.append(i)
		if tmp[3] == '1':
			lst2day.append(i)
		if tmp[2] == '1':
			lst3day.append(i)
		if tmp[1] == '1':
			lst4day.append(i)
		if tmp[0] == '1':
			lst5day.append(i)
	
	printlst(lst1day)
	printlst(lst2day)
	printlst(lst3day)
	printlst(lst4day)
	printlst(lst5day)

def printlst(lstday):
	i = 0
	for item in lstday:
		i += 1
		print("%3s" % item, end=" ")
		if i%4 == 0:
			print()

		


if __name__ == "__main__":
	genBirthday()
	# printSquare()

