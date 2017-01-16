#coding=utf-8
#引入模块'
import random
import sys

#游戏规则
winlist = [['石头','剪刀'],['剪刀','布'],['布','石头']]
#选择列表
choicelist = ['石头','剪刀','布']
#用户提示
prompt = '''可选项如下,
(0)石头
(1)剪刀
(2)布
(3)退出
请输入你的选择(输入数字即可) '''

while True:
	try:
		#保存用户输入的数字
		choicenum = int(input(prompt))
		#用户退出
		if choicenum == 3:
			#执行用户退出 跳出循环体
			break
		#用户选择之后和电脑比较  电脑的比较数据从哪来 随机产出数据
		comchoice = random.choice(choicelist)
		userchoice = choicelist[choicenum]
		bothchoice = [userchoice,comchoice]

		print('你选择了%s, 电脑选择了%s'%(userchoice,comchoice))
		#判断输赢
		if userchoice  == comchoice:
			print('打成平手')
		elif bothchoice in winlist:
			print('你赢了, 你厉害')
		else:
			print('你输了, 要不要再来一局')
	except(KeyboardInterrupt,EOFError,ValueError,IndexError):
		print('输入错误, 请重新输入')
		# sys.exit()
		pass
