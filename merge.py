a = raw_input()
m = input()

for i in xrange(len(a) / m):
	t = ''
	for c in a[i * m : (i + 1) * m]:
		if c in m:
			continue
		t += c
	print t

