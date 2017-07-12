from time import sleep
from requests import post

while True:
	try:
		r = post('https://noip.pouyacode.net/set', json={"name": "home"})
	except:
		log = open('noip.log','a')
		log.write('failed\n')
		log.close()
	sleep(600)