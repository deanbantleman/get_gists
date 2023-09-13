from github import Github

# Create a GitHub instance without providing a token
g = Github()

print('--------------------------------')
print('            Gist App')
print('--------------------------------')
print()

username = input('Enter the username you want to fetch gists from: ')

user = g.get_user(username)

print(user)

try:
    user = g.get_user(username)
    gists = user.get_gists()

    if gists:
        print(f"Gists for GitHub user: {username}\n")
        for gist in gists:
            print(gist)
            # print(f"ID: {gist.id}")
            # print(f"Description: {gist.description}")
            # print(f"URL: {gist.html_url}\n")
    else:
        print(f"No gists found for GitHub user: {username}")

except Exception as e:
    print(f"Error: {e}")