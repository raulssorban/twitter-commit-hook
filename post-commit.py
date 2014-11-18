import sys
from subprocess import call
from twython import Twython

APP_KEY = '[APP_KEY]'
APP_SECRET = '[APP_SECRET]' 
OAUTH_TOKEN = '[OAUTH_TOKEN]'
OAUTH_TOKEN_SECRET = '[OAUTH_TOKEN_SECRET]'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

if sys.argv[1] != sys.argv[2]:
	twitter.update_status(status=sys.argv[1])