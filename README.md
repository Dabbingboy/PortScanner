# PortScanner
Port scanner is a program which scans the port for the given IPv4 address, and checks if the given ports are open or not. This code can be used as directly in console like any other tool or as a module in some other code which just requires the funciton "scan_ports" in it thus, being multipurpose and user friendly    
Arguments: Hostname :- (IP or DNS), ports :- (1,2,3-5,6,7)  
it uses the following modules :- socket, argparse, sys and datetime  
socket:- Scan the target for the given ports  
argparse:- Take arguments as input, crucial for running the program on the console like any other tool  
sys:- Control the flow of the code  
datetime:- Calculate the time spent during the scan 
