import socket
import argparse
import sys
import datetime

def scanner(hosts,ports):
    for port in ports:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1.2)
            connection_status=s.connect_ex((hosts,port))#value
            if connection_status==0:
                print("Port: ",port,"is open")
            s.close()
        except KeyboardInterrupt:
            print("Can not proceed further #INTERUPTED_BY_USER")
            sys.exit()
        except socket.gaierror:
            print("#HOST_ERROR")
            sys.exit()
        except socket.error:
            print("#SERVER_ERROR")
            sys.exit()

def parse_ports(ports_input):
    ports=set()
    dirty_ports=ports_input.split(',')#converting "1,2,3" to "1","2","3" and "4-7" to "4","5","6","7"
    for i in dirty_ports:
        if '-' in i:
            st,end = i.split('-')
            st=int(st);end=int(end)
            ports.update(range(st,end+1))
        else:
            ports.add(int(i))
    return sorted(ports)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP port scanner")
    parser.add_argument("host", help= "Target IP address or Domain")
    parser.add_argument("-p","--ports", default = "20-1024" ,help= "Ports (20,80,443 or 20-32)")
    parser.add_argument("-f","--fast", action="store_true", help="Scan commonly open TCP ports")
    args = parser.parse_args()

    target = args.host
    if args.fast:
        ports=[21,22,23,25,53,69,80,110,143,161,443,514,631]
    else:
        ports = parse_ports(args.ports)

    start_time = datetime.datetime.now()
    scanner(target,ports)
    end_time = datetime.datetime.now()
    print("Time Taken to perform the scan: ",end_time-start_time)
