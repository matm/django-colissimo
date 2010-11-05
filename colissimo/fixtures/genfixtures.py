#!/usr/bin/env python

import sys, re

def main():
	"""
	Will output JSON initial data on stdout. Redirect the output to initial_data.json and 
	run syncdb to get the data loaded into the database.
	"""
	if len(sys.argv) != 2:
		print "Usage: %s rate_file.txt" % sys.argv[0]
		sys.exit(2)

	ratefile = sys.argv[1]
	f = open(ratefile)
	data = f.readlines()
	round = 0
	cmdidx = 1
	pattern = '  {"pk": %d, "model": "colissimo.%s", "fields": %s}'
	model = fields = None
	print "["
	for line in data:
		line = line[:-1]
		line = re.sub(r'#.*$', '', line).strip()
		# Skip comments
		if line.startswith('#') or len(line) == 0:
			continue
		if line.startswith('::'):
			last_model = model
			# Command
			line = line[2:].split(',')
			model, fields = line[0], line[1:]
			if last_model != None and last_model != model:
				cmdidx = 1
				round += 1
		else:
			if cmdidx == 1 and round == 0: 
				print
			else:
				print ','
			# Data line
			data = [fi.strip() for fi in line.split(',')]
			if len(data) != len(fields):
				raise ValueError, "Field length mismatch"
			dataset = {}
			for k in range(len(fields)):
				dataset[fields[k]] = data[k]
			out = pattern % (cmdidx, model, dataset)
			print out.replace("'", "\""),
			cmdidx += 1
	print "\n]"
	f.close()

if __name__ == '__main__':
	main()
