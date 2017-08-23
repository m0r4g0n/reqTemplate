import requests
import sys
import threading

nthreads=3

def myquery():
	URL = sys.argv[1]

	if not 'http' in URL:
		URL = 'http://'+URL

	r = requests.get(URL)
	print (r.status_code)
	print (r.headers['Set-Cookie'])

#threads = []

for i in range(nthreads):
	t = threading.Thread(target=myquery)
#	threads.append(t)
	t.start()
