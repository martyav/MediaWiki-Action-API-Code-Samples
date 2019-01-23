#!/usr/bin/python3

"""
    move.py

    MediaWiki Action API Code Samples
    Demo of `Move` module: Move a page.
    MIT license
"""

import requests

S = requests.Session()

URL = "https://www.thetestwiki.org/w/api.php"

# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
print(LOGIN_TOKEN)

# Step 2: Send a post request to log in. For this login 
# method, obtain credentials by first visiting
# https://www.test.wikipedia.org/wiki/Manual:Bot_passwords
# See https://www.mediawiki.org/wiki/API:Login for more
# information on log in methods.
PARAMS_2 = {
    "action": "login",
    "lgname": "user_name",
    "lgpassword": "password",
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)
DATA = R.json()

print(DATA)

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

print(CSRF_TOKEN)

# Step 4: Send a Post request to move the page
PARAMS_4 = {
    "action": "move",
    "format": "json",
    "from": "TestMove",
    "to": "Test Move",
    "reason": "Typo",
    "movetalk": "1",
    "noredirect": "1",
    "token": CSRF_TOKEN
}

HEADERS = {
    "Content-Type": "multipart/form-data",
    "Token": CSRF_TOKEN
}

EXAMINE=requests.Request("POST", url=URL, headers=HEADERS, data=PARAMS_4)
print(EXAMINE.prepare().body)

R = S.post(url=URL, data=PARAMS_4, headers=HEADERS)
DATA = R.json()

print(DATA)