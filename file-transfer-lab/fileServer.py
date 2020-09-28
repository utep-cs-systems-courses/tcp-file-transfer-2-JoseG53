#! /usr/bin/env python3

#Author: Jose Gallardo

import socket, sys, re

sys.path.append("../lib")
import params

switchesVarDefaults = (
    (('l', '--listenPort'), 'listenPort', 50001),
    (('-?', '--usage'),"usage", False), #bool set if present
)

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''

if paramMap['usage']:
    params.usage()