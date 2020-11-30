import nmap3
import json
import pprint
import socket
from LocalIP import returnIPNet


#will look for open ports on a network and return list of IPs with that open port
def ImprovedScanner(port, scanRange = 255,network = None): #network must be an iP address that ends in .0 ex 192.168.1.0

    maxIP = scanRange
    Avail_IP_List = []

    vendorDict = {}

    #Get IP network of local machine
    IP_network = returnIPNet()

    #if not ip address was added us the local IP
    if(network != None):
        IP_network = network

    #Grab Prefex
    IP_prefex = IP_network[:-1]

    #Start nmap connection
    nmap = nmap3.NmapScanTechniques()




    #ping all ips in network and generate list of machines 
    for location in range(1,maxIP):
        IP_Address = IP_prefex + str(location)
        results = nmap.nmap_ping_scan(IP_Address)
        print("Pinging " + IP_Address + " ...", end='')
        
        try:
            data = results[0]
            print()
            Avail_IP_List.append(IP_Address)
            vendorDict[IP_Address] = ""
            print("Machine found at " + IP_Address + "...",end='')
        except:
            print(" no machine ",end='')


        try:
            data = results[0]
            vendorInfo = data['addresses'][1]['vendor']
            vendorDict[IP_Address] = vendorInfo
            print(" made by " + vendorInfo)
        except:
            print(" no vendor")
            

    
    #port scanning phase

    ports = nmap3.Nmap()
    print("Port " + str(port) + " scan")
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    openPortList = []


    #scan for open port useing list of active machines
    for IPs in Avail_IP_List:
        location = (IPs, port)
        result_of_check = a_socket.connect_ex(location)

        print(result_of_check)

        if result_of_check == 0:
           print("Port " + str(port) + " on " + IPs + " is open adding to list")
           openPortList.append(IPs)
        else:
           print("Port on " + IPs + " is not open")
        

    a_socket.close()

    return openPortList, Avail_IP_List, vendorDict



