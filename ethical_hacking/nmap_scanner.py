import nmap
import json


scanner = nmap.PortScanner()
nmap_output = str(scanner.scan('192.168.178.1', '1-20', '-sn'))
print(nmap_output)
