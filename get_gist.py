#!/usr/bin/env python3

# get_gist queries public gists, one user at a time :)
#
# Syntax: # get_gist <username>
#
# Where <username> is a valid GitHub username.
# Can use public user: PlugFox
# The first time you query a user the script will display all gists
# for that user. A user file will be created in the same working directory
# named "./pygist.<username>". Subsequent executions for the same username 
# will only show gists published since the last run. 

import os
import argparse
import json
import requests
from datetime import datetime
from pprintpp import pprint

parser = argparse.ArgumentParser()
parser.add_argument("username", help="GitHub username")
args = parser.parse_args()
github_gists_url = 'http://api.github.com/users/' + args.username + '/gists'

gists = []

page = 1
while True:
    params = {'page': page}
    with requests.get(github_gists_url, params=params) as r:
        if r.status_code != 200:
            if r.status_code == 404:
                pprint('Error: GitHub user "' + args.username + '" not found.')
            else:
                r.raise_for_status()
                exit(255)
        page_gists = r.json()
        if not page_gists:
            break  # No more gists to retrieve
        gists.extend(page_gists)
        page += 1

if not gists:
    pprint('GitHub user "' + args.username + '" has not published any gists.')
    exit(1)

config_file = './pygist.' + args.username

if not os.path.isfile(config_file):
    print('No previous entries for user "' + args.username + '"')
    print('Creating user file: ' + config_file)
    for item in gists:
        pprint("Created Date: " + item["created_at"] + " URL: " + item["html_url"])
    try:
        with open(config_file, 'w') as user_file:
            user_file.write(gists[0]['created_at'])
    except Exception as e:
        raise
else:
    try:
        with open(config_file, 'r') as user_file:
            last_query = user_file.read()
    except Exception as e:
        raise
    last_query_time = datetime.strptime(last_query, '%Y-%m-%dT%H:%M:%SZ')
    gist_created_date = datetime.strptime(gists[0]['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    if gist_created_date > last_query_time:
        print('User "' + args.username + '" has created new gist(s) since the last query.')

        for item in gists:
            item_created_at = datetime.strptime(item["created_at"], '%Y-%m-%dT%H:%M:%SZ')
            if item_created_at > last_query_time:
                pprint("Created Date: " + item["created_at"] + " URL: " + item["html_url"])

        try:
            with open(config_file, 'r') as user_file:
                user_file.seek(0, 0)
            with open(config_file, 'w') as user_file:
                user_file.write(gists[0]['created_at'])
        except Exception as e:
            raise
    else:
        print('User "' + args.username + '" has not created any new gists since the last query.')
exit(0)