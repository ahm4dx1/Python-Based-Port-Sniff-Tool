#Port-Sniff Tool

from argparse import ArgumentParser
import socket
from threading import Thread
from time import time
import scapy.all as scapy
from scapy.layers import http
from colorama import Fore

open_ports = []

def prepare_arg():
    parser = ArgumentParser(description="Python based Fast Ports scanner and Packet Sniffer", usage="%(prog)s -m [scan/sniff] -i 192.168.1.2")
    parser.add_argument("-m", "--mode", dest="mode", choices=['scan', 'sniff'], help="Choose mode: scan or sniff")
    parser.add_argument("-i", "--ip", dest="ip", metavar='\b', help='IPv4 address')
    parser.add_argument("-s", "--start", dest="start", metavar='\b', type=int, help="starting port", default=1)
    parser.add_argument('-e', '--end', dest='end', metavar='\b', type=int, help="ending port", default=500)
    parser.add_argument('-t', '--threads', dest='thread', metavar='\b', type=int, help="threads to use", default=500)
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='verbose output')
    parser.add_argument('-V', '--version', dest='version', action='version', version='%(prog)s 3.0', help='Display version')
    arguments = parser.parse_args()
    return arguments

#it is used to iterate over port during scan
def prep_port(start: int, end: int):
    for ports in range(start, end + 1):
        yield ports

def prep_thread(thread: int):
    thread_list = []
    for _ in range(thread + 1):
        thread_list.append(Thread(target=scan_port))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

def scan_port():
    while True:
        try:
            s = socket.socket()
            s.settimeout(1)
            port = next(ports)
            s.connect((arguments.ip, port))
            open_ports.append(port)
            if arguments.verbose:
                print(f'\r{open_ports}', end='')
        except (ConnectionRefusedError, socket.timeout):
            continue
        except StopIteration:
            break

def sniff(iface):
    try:
        scapy.sniff(iface=iface, store=False, prn=process_packet)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+] HTTP request >> " + (packet[http.HTTPRequest].Host).decode('utf-8') + (packet[http.HTTPRequest].Path).decode('utf-8'))
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = (["username".encode('utf-8'), "password".encode('utf-8'), "pass".encode('utf-8'), "email".encode('utf-8')])
            for key in keys:
                if key in load:
                    print(Fore.GREEN + "\n\n\n\[+] Possible username\password >>" + load.decode('utf-8') + "\n\n\n")
                    break
if __name__ == "__main__":
    arguments = prepare_arg()

    if arguments.mode == 'scan':
        ports = prep_port(arguments.start, arguments.end)
        start_time = time()
        threads = prep_thread(arguments.thread)
        end_time = time()

        if not open_ports:
            print("All ports are closed.")
        else:
            print(f"\nOpen Ports Found - {open_ports}")

        # Always display the time taken for scanning
        print(f'Time taken - {round(end_time - start_time, 3)}')

    elif arguments.mode == 'sniff':
        iface = arguments.ip  # Use the IP argument for the interface
        if iface:
            sniff(iface)
        else:
            print("Please provide a valid network interface for sniffing.")
    else:
        print("Invalid mode selected. Use 'scan' or 'sniff'.")
