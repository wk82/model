#练习1 100内奇数和
#i=0
#result=0
#while i <100 :
#	i += 1
#	#判断i是否是奇数
#	if i % 2 != 0 :
#		result += i
#print('result =',result)


#练习2 1000内所有的水仙花数
#水仙花指一个n位数（n>=3），它的每个位上的数字n次幂之和等于它本身
#获取1000以内的三位数
#i = 100
#while i <1000
##假设i的百位是a，十位是b，个位是c
##求i的百位数
#	a = i //100
##求i的十位数
##b = i//10%10
#	b = (i - a*100)//10
##求i的个位
#	c = i % 10
#	if a**3 + b**3 + c**3 == i :
#		print(i)
#	i += 1
 
# 练习3 判断用户输入的任意数是否是质数
# num = int(input('输入任意大于1的整数：'))
# #判断num是否是质数，只能被1和它自身整除的数
# #获取到所有的问题可能整除的整数
# i = 2
# #创建一个变量，用来记录是否是质数，默认是质数
# flag = True
# while i < num :
# 	#判断num是否被i整除
# 	#如果num能被整除，则说明num一定不是质数
# 	if num % i == 0 :
# 		#一旦进入判断，则说明num不是质数，需要将flag改为false
# 		flag = False
# 	i += 1
# if flag :
# 	print(num,'是质数')
# else :
# 	print(num,'不是质数')

#练习4 创建一个循环来控制图形的高度
#循环嵌套时，外层循环执行一次，内层循环就执行一圈
#i=0
#while i < 5 :
#	#创建一个内层循环控制图形宽度
#	j=0
#	while j < 5 :
#		print("* ",end='') # end='' 表示结尾不使用换行符
#		j += 1
#	print()   #打印一个换行符
#	i +=1

#练习5 正三角
#i=0
#while i < 5 :
##	#创建一个内层循环控制图形宽度
#	j=0
#	while j < i + 1  :
#		print("* ",end='') # end='' 表示结尾不使用换行符
#		j += 1
#	print()   #打印一个换行符
#	i +=1

#练习6 倒三角
#i=0
#while i < 5 :
##	#创建一个内层循环控制图形宽度
#	j=0
#	while j < 5 - i :
#		print("* ",end='') # end='' 表示结尾不使用换行符
#		j += 1
#	print()   #打印一个换行符
#	i +=1
 	
#练习7 乘法口诀表
#方法1:自己的方法
#i = 1
#while i <= 9 :
#	j = 1
#	while j <= i :
#		result = i * j
#		print(i,"*",j,"=",result," ",end='')
#		j += 1
#	print()
#	i +=1
#方法2:示例
#i=0
#while i < 9 :
#	i += 1
#	j = 0
#	while j < i :
#		j += 1
#		print(f"{j}*{i}={i*j}"," ",end="")
#	print()

#练习8 求100内所有的质数
#创建一个循环,求1-100内所有的数
i=2
while i <= 100:
	#创建一个变量,记录i的状态,默认i是质数
	flag=True
	#判断i是否是质数
	#获取所有可能成为i的因数的数
	j=2
	while j < i:
		#判断i是否被j整除
		if i % j ==0:
			#i能被j整除,证明i不是质数,修改flag为false
			flag = False
		j +=1
	#验证结果并输出
	if flag :
		print (i)
	i += 1
