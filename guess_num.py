import random
ans = random.randint(1,100)
while True:
	number = input('請輸入數字： ')
	number = int(number)
	if number == ans:
		print('恭喜猜對了！')
		break
	elif number > ans:
		print('比答案大')
	else:
		print('比答案小')