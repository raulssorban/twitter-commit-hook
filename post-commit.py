import sys
from json

from twython import Twython

with open('keys.json') as file:
	keys = json.load(file)

twitter = Twython(keys['APP_KEY'], keys['APP_SECRET'], keys['ACCESS_TOKEN'], keys['ACCESS_TOKEN_SECRET'])

if sys.argv[2] != sys.argv[3]:
	message = sys.argv[1] + ': ' + sys.argv[2]
	if len(message) > 140:
		message = message[:137] + '...'
	twitter.update_status(status=message)
