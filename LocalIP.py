import socket



def returnIPNet():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localIP = s.getsockname()[0]
    s.close
    localIPList = localIP.split(".")
    network = localIPList[0] + "." + localIPList[1] +"."+ localIPList[2] + "." + "0"
    print(network)
    return network



