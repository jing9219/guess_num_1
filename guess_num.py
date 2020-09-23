import random
start = input('請決定隨機數字範圍起始值： ')
end = input('請決定隨機數字範圍結束值： ')
start = int(start)
end = int(end)

ans = random.randint(start,end)
count = 0
while True:
	count += 1 # count = count + 1
	number = input('請輸入數字： ')
	number = int(number)
	if number == ans:
		print('恭喜猜對了！')
		print('這是你猜的第', count, '次')
		break
	elif number > ans:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count, '次')