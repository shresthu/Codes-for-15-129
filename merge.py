s = raw_input()
k = input()

for i in xrange(len(s) / k):
	t = ''
	for c in s[i * k : (i + 1) * k]:
		if c in t:
			continue
		t += c
	print t

