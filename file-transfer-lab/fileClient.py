#! /usr/bin/env python3

#Author: Jose Gallardo


import socket, sys, re, os

sys.path.append("../lib") #for params
import params

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-?', '--usage'), "usage", False), # bool set if present
)

progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Cant parse server:port from '%s'" % server)
    sys.exit(1)
    
