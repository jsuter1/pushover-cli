#!/usr/bin/python3

"""
Pushover-CLI

A single-file Python script to send Pushover notifications via the command line.

Copyright 2014, Jack Suter. Released under the MIT license.

"""
import http.client, urllib     #Pushover communication
import argparse                #CLI argument parsing
from socket import gethostname #Default notification title
# from sys import exit

# User Configuration
APP_TOKEN = "APP_TOKEN_HERE"
USER_KEY = "USER_KEY_HERE"

# Arguments
parser = argparse.ArgumentParser(description='Pushover notification gateway')
parser.add_argument('message', help='Pushover message')
parser.add_argument('--priority', default="0", help='Message Priority. '+
    '-1 quiet; 0 default, 1 high; 2 emergency')
parser.add_argument('--title', default=gethostname(), help='Message title. '+
    'Defaults to system hostname ('+gethostname()+')')
parser.add_argument('--sound', default="pushover", help='Message Sound. See '+
    'https://pushover.net/api#sounds')
parser.add_argument('--quiet', action='store_true', help='Use return codes '+
    'instead of text')
args = parser.parse_args()

Push = ({
    "token":	APP_TOKEN,
    "user":	USER_KEY,
    "sound":	args.sound,
})

Push["message"] = args.message
Push["title"] = args.title

# Message Priority
# -1	Quiet notification
#  0	Default notification
#  1	High Priority
#  2	Emergency, retry until acknowledged

Push["priority"] = args.priority
if args.priority == "2":
    Push["sound"] = "persistent"
    Push["retry"] = 30			#Retry every 30 seconds
    Push["expire"] = 86400		#for 24 hours
    #Push["callback"] = "http://"	#Callback notification

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode(Push), {
        "Content-type": "application/x-www-form-urlencoded"
    }
)
response = conn.getresponse()

if response.status == 200:
    if args.quiet:
        exit(True)
    else:
        print("Notification sent!")
else:
    if args.quiet:
        exit(False)
    else:
        print(response.status, response.reason)
        print(response.read())
