import os 
import sys
from nester import print_lol

luj = os.getcwd()
print(luj)
man = []
other = []

try:
	data = open('sketch2.txt')

	data.seek(0)
	for each_line in data:
		try:
			each_line = each_line.strip('\n')
			(role,line_spoken) = each_line.split(':',1)
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	
	data.close()
except IOError:
	print('The data file is missing!')

try:
	with open('man_data.txt','w') as man_file,open('other_data.txt','w') as other_file:
		print_lol(man,fn=man_file)
		print_lol(other,fn=other_file)

except IOError as err:
	print('File error' + str(err))
