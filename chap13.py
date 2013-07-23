import sys
import string
import random

suffix_map = {}    #dictionarie
prefix = ()        #tuple

def process_file(filename, order=2):
	fp = open(filename)
	skip_gutenberg_header(fp)

	for line in fp:
		for word in line.rstrip().split():
			process_word(word, order)

def skip_gutenberg_header(fp):
	for line in fp:
		if line.startswith('*END*THE SMALL PRINT!'):
			break

def process_word(word, order=2):
	global prefix
	if len(prefix) < order:
		prefix += (word,)
		return

	try:
		suffix_map[prefix].append(word)
	except KeyError:
		suffix_map[prefix] = [word]

	prefix = shift(prefix, word)

def random_text(n=100):
	start = random.choice(suffix_map.keys())

	for i in range(n):
		suffixes = suffix_map.get(start, None)
		if suffix_map == None:
			random_text(n-i)
			return

		word = random.choice(suffixes)
		print word, 
		start = shift(start, word)

def shift(t, word):
	return t[1:] + (word,)

def main(name, filename='emma.txt', n=100, order=5, *args):
	try:
		n = int(n)
		order = int(order)
	except:
		print 'Usage: randomtext.py filename [# of words] [prefix length]'
	else: process_file(filename, order)
	random_text(n)


if __name__ == '__main__':
	main(*sys.argv)