def get_lines(name_file):
	# return open(name_file, 'r').readlines()
	f = open(name_file, 'r')
	lines = f.read().split('\n')
	f.close()
	return lines


def get_dict_tuple(name_file, height):
	lines = get_lines(name_file)
	d = {}
	for pos in range(0, len(lines), height+1):
		dig = lines[pos]
		d[dig] = tuple(lines[pos+1:pos+height+1])
	return d


def get_dict_list(name_file, height):
	lines = get_lines(name_file)
	d = {}
	for pos in range(0, len(lines), height+1):
		dig = lines[pos]
		d[dig] = lines[pos+1:pos+height+1]
	return d


def get_dict_str(name_file, height):
	lines = get_lines(name_file)
	d = {}
	for pos in range(0, len(lines), height+1):
		dig = lines[pos]
		d[dig] = ''.join(lines[pos+1:pos+height+1])
	return d
