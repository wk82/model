#显示欢迎信息
print ('-'*20,'欢迎光临<唐僧大战白骨精>','-'*20)
#显示身份信息
print('请输入你的身份:')
print('\t1.唐僧')
print('\t2.白骨精')
#游戏的身份选择
player_choose = input ('请选择[1-2]:')
#打印分割线
print('-'*66)
#根据用户选择显示不同的提示信息
if player_choose == '1':
	print('你已经选择了1,你将以唐僧的身份进行游戏!')
elif player_choose == '2' :
    print('你竟然选择白骨精,你还是以唐僧身份来进行游戏!')
else :
	print ('你的输入有误,系统自动分配,你将以唐僧的身份进行游戏!')
#进入游戏
#创建变量,保存玩家的生命值和攻击力
player_life = 2 
player_attack = 2
#创建变量,保存boss的生命值和攻击力
boss_life = 10
boss_attack = 10
#打印分割线
print('-'*66)
#显示玩家的信息
print(f'唐僧的生命值{player_life},你的攻击力是{player_attack}')
#由于游戏选项需要反复显示,必须编写到一个循环中
while True : #重复循环
    #打印分割线
    print('-'*66)
    #显示游戏选项
    print('请选择你要进行的操作:')
    print('\t1.练级')
    print('\t2.打BOSS')
    print('\t3.逃跑')
    game_choose = input('请选择要做的操作[1-3]:')
    #处理用户的选择
    if game_choose == '1' :
    	#增加玩家的生命力攻击力
    	player_life += 2
    	player_attack += 2
    	print('-'*66)
    	#显示玩家信息
    	print(f'恭喜你升级,你现在的生命值是{player_life},你的攻击力是{player_attack}')
    elif game_choose == '2' :
    	#玩家攻击boss
    	#减去boss的生命值
    	boss_life -= player_attack
    	#打印分割线
    	print('-'*66)
    	print('唐僧攻击白骨精')
        #检查boss是否死亡
    	if boss_life <= 0 :

    		print(f'白骨精受到{player_attack}点伤害,死掉,唐僧胜利!')
        	#游戏结束
    		break 
        #boss反击玩家
        #减去玩家的生命值
    	player_life -= boss_attack
    	print('白骨精攻击唐僧')
        #检查玩家是否死亡
    	if player_life <=0 :

        	#玩家死亡
    		print(f'受到了{boss_attack}点伤害,死了,game over!')
        	#游戏结束
    		break
    elif game_choose =='3' :
    	print('唐僧跑了,game over')
    	break
    else :
    	print('输入有误,重新输入')