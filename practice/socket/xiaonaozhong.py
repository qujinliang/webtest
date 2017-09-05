from datetime import datetime

import os

loop = True

while(loop):
	now = datetime.now()
	weekday = now.strftime('%w')
	hour = now.strftime('%H')
	minute = now.strftime('%M')

	if hour == '22' and minute =='30':
		os.startfile(r'/应用程序/QQMusic.app')
		loop = False
	else:
		pass
		