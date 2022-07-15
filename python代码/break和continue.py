#break可用来立即退出循环语句(包括else)
#continue 可用来跳过当次循环
#break 和 continue 只对离最近的循环起作用
#pass 用来在判断或循环语句中占位的
#i = 0
#while i < 5 :
#	if i == 3:
#		break 
#	print (i)
#	i += 1
#else :
#	print ('循环结束')

i = 0
while i < 5:
	i += 1
	if i == 2:
		continue
	print(i)
else :
	print ('循环结束')