import sys
from twython import Twython

APP_KEY = '[APP_KEY]'
APP_SECRET = '[APP_SECRET]' 
ACCESS_TOKEN = '[ACCESS_TOKEN]'
ACCESS_TOKEN_SECRET = '[ACCESS_TOKEN_SECRET]'

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

if sys.argv[2] != sys.argv[3]:
	message = sys.argv[1] + ': ' + sys.argv[2]
	if len(message) > 140:
		message = message[:137] + '...'
	twitter.update_status(status=message)