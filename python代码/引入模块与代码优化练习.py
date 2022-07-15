#通过模块可以对python进行扩展
#引入一个time模块,统计程序执行的时间
#通过算法减少数据处理，提升性能
from time import *
#time ()函数可以用来获取当前时间,返回单位是秒
begin = time ()

i=2
while i <= 100000:
	flag=True
	j=2
	while j <= i**0.5: #第二次优化
		if i % j ==0:
			flag = False
			#进入判断，则证明i一定不是质数，此时内层循环没有继续必要
			#使用break来退出内层循环
			break #第一次优化
		j +=1
	if flag :
	    pass #print (i) 
	i += 1
end = time()
#计算程序执行的时间
print ("程序执行花费了:",end - begin ,"秒")