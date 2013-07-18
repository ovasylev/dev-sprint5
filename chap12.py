#1.

def anagrams(file):
	fo = open(file, 'r')
	anagram_list = {}
	for line in fo:
		word = line.strip()
		s = list(word)    # convert string into a list
		s.sort()
		s = ''.join(s)
		if s not in anagram_list:
			anagram_list[s] = [word]
		else:
			anagram_list[s].append(word)
	return anagram_list

print anagrams('test.txt')

#-----test.txt-------
# deltas
# desalt
# lasted
# salted
# slated
# staled
# retainers
# ternaries
# resmelts
# smelters
# termless

#------Result:-----
#2 [['retainers', 'ternaries'], 
#6 ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'], 
#3 ['resmelts', 'smelters', 'termless']]

#2.
def pas_in_order(file):
	ordered_set = []
	l = anagrams(file)
	for v in l:
		if len(v) > 1:
			ordered_set.append((len(v), v))
	ordered_set.sort()
	for item in ordered_set:
		print item[1]

pas_in_order('test.txt')

#-----Result:-----
# ['retainers', 'ternaries']
# ['resmelts', 'smelters', 'termless']
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']

#3.
def scrabble(file, n):
	res = {}
	d = anagrams(file)
	for word, anagram in d.iteritems():
		#print word, anagrams
		if len(word) == n:
			res[word] = anagram
	return res.values()

print scrabble('test.txt', 8)

#------Result:------
# [['resmelts', 'smelters', 'termless']]



