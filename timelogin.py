import urllib
import urllib2
import time
import scipy.stats
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

url = 'http://localhost/login.php'

values = {	'username':'sdfasdfs',
		'password':'sdfasdfa',
		'Login':'Login'}

print "Invalid user"

result1 = []
for i in xrange(1000):
	start_time = time.time()
	x = opener.open(url)
	result1.append(time.time() - start_time)
	x.close()
print reduce(lambda x, y: x + y, result1) / len(result1)

values = {	'username':'admin',
		'password':'password',
		'Login':'Login'}

print "Valid user"

result2 = []
for i in xrange(1000):
	start_time = time.time()
	opener.open(url)
	result2.append(time.time() - start_time)
	x.close()	
print reduce(lambda x, y: x + y, result2) / len(result2)

f, p = scipy.stats.f_oneway(result1, result2)
if f > 3.936:
	print 'f = %f > 3.936 implies results ARE DIFFERENT' % f
else:
	print 'f = %f < 3.936 implies results ARE EQUAL' % f
		

if p < 0.05:
	print 'p = %f < 0.05 implies results ARE DIFFERENT' % p
else:
	print 'p = %f > 0.05 implies results ARE EQUAL' % p
