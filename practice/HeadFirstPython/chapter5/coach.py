def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'

	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' + secs)

# with open('james.txt') as jaf:
# 	data = jaf.readline()
# james = data.strip().split(',')

# with open('julie.txt') as juf:
# 	data = juf.readline()
# julie = data.strip().split(',')

# with open('mikey.txt') as mif:
# 	data = mif.readline()
# mikey = data.strip().split(',')

# with open('sarah.txt') as asf:
# 	data = asf.readline()
# sarah = data.strip().split(',')

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = (data.strip().split(','))
		return({'Name' : templ.pop(0),
			'DOB' : templ.pop(0),
			'Times' : str(sorted(set([sanitize(t) for t in templ]))[0:3])})
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)


james = get_coach_data('james.txt')
sarah = get_coach_data('sarah.txt')


#clear_james = sorted(set([sanitize(each_t) for each_t in james]))[0:3]
#clear_julie = sorted(set([sanitize(each_t) for each_t in julie]))[0:3]
#clear_mikey = sorted(set([sanitize(each_t) for each_t in mikey]))[0:3]



print(james['Name'] + "' s fastest times are: " + james['Times'])

