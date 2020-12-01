Web Hack Application

## Installation

Setup instructions

Download repository

sudo apt update

sudo apt purge python2.7-minimal

sudo apt-get install python3

sudo apt install python3.tk

sudo apt-get insatll pip3


PATH $PATH:/home/pi/.local/bin or add it manually to .bashrc

open terminal and navigate to repository

sudo apt install nmap

pip install python3-nmap

pip3 install -r requirements

Raspberry Pi Network Hacker? Login Hacker? ![](Info%203150%20Project%20documentation%20text.001.png)

**ABSTRACT** 

Penetration testing is an important part of security for many businesses, and with the prevalence of WiFi in many modern business settings, low cost methods of penetration testing may be desired. The Raspberry Pi 4 is a low cost computer with Bluetooth and WiFi capability, excellent for simple penetration testing. Our program runs on Python with a bit of JavaScript for testing. 

**INTRODUCTION** 

A program written in python that will run on a Raspberry Pi, uses the built in wireless network adapter to check through all devices on a network, and list any with open ports. The user will select one and with a user-provided login url, like what an IP camera or printer would use, it will try to connect to the device with a brute force attack and then return the username and password combination that worked. 

**CONCEPTS** 

Network Scanning** 

The scanning module takes in a port number with optional arguments for network scan range and a network address. If the module does not receive a network address nor a scan range, it defaults to the network address of the machine it is on and scans from .1 to .254. The module first builds a list of all active IPs on the network and loads all of those IPs into a dictionary that returns the vendor name of the machine, if available. If not available, the vendor dictionary returns a blank space. Once it has created a list of all IPs on the network it then attempts to connect to those IPs on the user-defined port. It uses these connection attempts to generate a list of machines for which that port is accepting connection. Finally the scanning module returns a list of IPs with the open port, a list of IPs with an active machine on them and a dictionary with active IPs as the key and vendor name as the value. There is also a second scanning module 

available which simply returns a list of IPs with a particular open port. 

Brute Force Attack 

A brute-force attack in cryptography involves the attacker sending many login attempts and hoping to eventually guess the correct combination of username and password. For our brute-force password attack methodology, we attempted to implement it in two ways. In  our login\_brute\_force.py script we accept multiple input parameters such as url, username format, and password format. The url parameter must include the application layer protocol being used, such as “http://”. Similarly, the url can also accept an ip and port number so long as an application layer protocol is preceding it. On the other hand, the username format and password format are provided by the user based on what html attribute the login page returns to its server. The html attribute information can be obtained by inspecting the login page itself and finding what the input attributes for each username and password are. Once all those information are passed to login\_brute\_force.py, the script attempts to establish connection using a combination of the username and password dictionary lists and returns back the information for the successful login attempt. Moreover, as the dictionary lists are saved as text files their contents can be updated and changed as the user wishes outside the program. The second brute force implementation we attempted was to do SSH brute-force using the parameters of ip and port numbers. Similarly, ssh\_brute\_force.py uses dictionary text files for passwords and usernames[1]. If the ssh attempt is successful then the username host and password are returned and displayed. On the other hand if there is no port connection then we notify the user that the port is not open. Similarly, if the username and password lists are exhausted we notify the user with our failure. ![](Info%203150%20Project%20documentation%20text.001.png)

**SYSTEM HARDWARE DESIGN** 

The Raspberry Pi 4 uses a Broadcom BCM2711 SoC with a 1.5GHz 64-bit quad-core ARM Cortex-A72 processor. It has an on board WiFi adapter supporting dual band IEEE 802.11ac WiFi, as well as a Gigabit Ethernet port. The Raspberry Pi is installed with a MicroSD card that acts as long term storage. The MicroSD card is preloaded with NOOBS (New Out of Box Software) to install the operating system. 

**METHODOLOGY (INSTALLATION)** 

Our methodology uses the Raspberry Pi with a connected monitor and keyboard. We used a Raspberry Pi 4 Model B starter kit bought from CanaKit, with the latest version of Raspberry Pi OS. After the OS has been installed and the monitor and keyboard connected, turn on the power, and the board will begin to boot up. 

After the board has booted and the user has logged in, get the repository from https://github.com/ramadawn/RasberriPi-WebHacket. Additionally some packages need to be installed so the program will work correctly. Installation commands are listed in the README.md file in the main repo, and the README.md file in the auth-server folder. Open a terminal, and navigate to the repo directory. From there use the command 

python3 main.py 

A user interface will open. Enter the network address to scan, or leave blank to scan the network the Pi is connected to. Enter the port you wish to test. Click Scan Network, and after some time a list of available devices will be shown. Select a cracking method from the dropdown box, either HTTP/HTTPS or SSH. HTTP/HTTPS uses a user-defined URL as it’s prefix, as well as user-defined username and password segments. If using SSH, provide an IP address in the URL field, and a port number in the Port field. Click Scan, and after some time, the program will display in the Results box either the successful username and password combination, or a formatted string indicating success, based on the selected cracking method. If using our included dummy node.js, the URL entered should be “http://127.0.0.1:3000/auth”, the 

username format “username”, and the password format “password”. 

**RESULTS** 

We used node.js to simulate a login server for testing purposes, as finding actual devices with login pages simple and predictable enough for our purposes proved difficult. 

**CONCLUSION** 

We set out to make a small hacking tool for a Raspberry Pi, and while we achieved that, there are many things we could improve on in the future, such as the speed of the program, the ease of installation, and the portability and flexibility of the system. The system is very limited as it is now, with ![](Info%203150%20Project%20documentation%20text.002.png)a great deal of its functionality needing to be manually operated. 

**REFERENCES** 

“*Code for How to Brute-Force SSH Servers in Python Tutorial”* Feb 15, 2020. Accessed on: Nov 30, 2020. [Online] Available: https://www.thepythoncode.com/code/brute-force-ssh-servers-using-paramiko-in-python* 

Dravicenna, *Port Scanner Multithreading port scanner with tkinter GUI*, Dec 20, 2019. Accessed on: Nov 30, 2020. [Online] Available: https://github.com/dravicenna/portscanner 



