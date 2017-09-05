while True:
	print("请输入你的分数：")
	score = float(input())
	if score <60:
		print('你的等级是D')
	elif 60 <= score < 80:
		print('你的等级是C')
	elif 80 <= score < 90:
		print('你的等级是B')
	else:
		print('你的等级A')
	print('回复Y继续查询')
	response = input()
	if response != 'Y':
		break
