import os 
import sys
import pickle
from nester import print_lol

luj = os.getcwd()
print(luj)
man = []
other = []
new_man=[]

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
	with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
		pickle.dump(man,man_file)
		pickle.dump(other,other_file)

except IOError as err:
	print('File error' + str(err))

except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))

try:
	with open('man_data.txt','rb') as man_file,open('other_data.txt','rb') as other_file:
		new_man = pickle.load(man_file)
		

except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print("Pickling error: " + str(perr))

