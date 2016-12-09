#!/usr/bin/python3
# TP-Link Dir Traversal Vulnerability Scanner
# Version 0.01
# Written by Humberto Jr

import nmap

print('TP-Link Scan v0,01 (Eg: 192.168.0.0/24)')
lista = input('Enter IP or Network/CIDR: ')

nmapcommand = nmap.PortScanner()
resultado=nmapcommand.scan(hosts=lista, arguments='-sV -p80 --script http-tplink-dir-traversal')


for x in nmapcommand.all_hosts():
    if '80' in str(nmapcommand[x]['tcp']):
        if 'script' in str(nmapcommand[x]['tcp'][80]) and 'VULNERABLE' in str(nmapcommand[x]['tcp'][80]['script']['http-tplink-dir-traversal']):
            print('[+] {0} : {1} - {2}'.format(x, nmapcommand[x]['tcp'][80]['product'], 'VULNERABLE'))
        else:
            print('[+] {0} : {1} '.format(x, nmapcommand[x]['tcp'][80]['product']))
    else:
        print('[-] {0} '.format(x))

