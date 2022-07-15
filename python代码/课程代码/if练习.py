#练习1  获取用户输入的整数，判断是奇数还是偶数
num = int(input('请输入任意整数：'))
#通过取模运算判断是奇数还是偶数
if num % 2 == 0 :
	print(num,"是偶数")
else :
	print(num,"是奇数")

#练习2 判断年份是否是闰年
#可以被4整除不能被100整除，或者可以被400整除
year = int(input("输入任意年份："))
if year % 4 ==0 and year % 100 !=0 or year % 400 ==0 :
	print (year,'闰年')
else :
	print (year,'平年')

#练习3 计算狗的年龄
#2岁前每年相当于人10.5，2岁后每年相当于人4岁
dog_age = float(input("输入狗的年龄："))
like_person_age = 0
#检查输入是否合法
if dog_age >0 :
	#如果狗年龄小于等于2岁
	if dog_age <= 2 :
		#将当前年龄乘以10.5
		like_person_age = dog_age * 10.5
	#如果狗的年龄两岁以上
    else :
    	like_person_age = 2 * 10.5
    	like_person_age += ( dog_age -2 ) *4
    
    print(dog_age,'岁的狗，相当于',like_person_age,'岁的人')
else :
	print ('输入合法年龄！')