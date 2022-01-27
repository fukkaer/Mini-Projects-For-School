# -*- coding: cp1252 -*-
print('words in an alphabetical order:')
with open('words.txt') as r:
	for line in sorted(r):
		print(line, end='')
