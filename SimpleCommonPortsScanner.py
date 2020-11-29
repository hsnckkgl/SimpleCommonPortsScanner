import sys #for command line argument
import nmap

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080] #add more ports

scanner = nmap.PortScanner()

print("\nScanning",target,"for ports 21,22,80,139,443,8080...\n")

for port in ports:
    portscan = scanner.scan(target,str(port))
    print("Port",port," is ",portscan["scan"][target]["tcp"][port]["state"])

print("\nHost",target," is ",portscan["scan"][target]["status"]["state"])
