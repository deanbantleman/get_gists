import requests
import json
import datetime

# Replace with your GitHub username or the username you want to fetch gists from
username = "deanbantleman"

# GitHub API endpoint for listing gists by a user
url = f"https://api.github.com/users/{username}/gists"

try:
    response = requests.get(url)
    # print(response.text)
    response.raise_for_status()  # Raise an exception if the request fails

    # Parse the JSON response
    gists = json.loads(response.text)
    print(gists)

    if gists:
        print(f"Gists for GitHub user: {username}\n")
        for gist in gists:
            print(f"ID: {gist['id']}")
            print(f"Description: {gist['description']}")
            print(f"URL: {gist['html_url']}\n")
            print(f"Created at: {gist['created_at']}")
            
    else:
        print(f"No gists found for GitHub user: {username}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")

