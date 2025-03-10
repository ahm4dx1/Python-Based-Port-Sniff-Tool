# 🚀 Port-Sniff Tool

## 📌 Description
Port-Sniff is a Python-based tool designed for fast port scanning and packet sniffing. It allows users to scan open ports on a given IP address and capture HTTP traffic to identify possible sensitive data.

## 🌟 Features
✅ **Fast Port Scanning**: Quickly scan a range of ports using multithreading.  
✅ **Packet Sniffing**: Capture HTTP requests and extract possible usernames and passwords.  
✅ **Verbose Mode**: Provides detailed output for scanning results.  
✅ **Customizable Port Range**: Allows users to specify start and end ports.  

## 📦 Prerequisites
Before running the script, ensure you have the required dependencies installed:

```sh
pip install scapy colorama
```

## 🛠️ Usage
Run the script with the appropriate options.

### 🔍 Port Scanning Mode
To scan for open ports on a target IP address:

```sh
python port_sniff.py -m scan -i <IP_ADDRESS> [-s <START_PORT>] [-e <END_PORT>] [-t <THREADS>] [-v]
```

#### 📝 Arguments:
- `-m, --mode` : Mode selection (`scan` or `sniff`).
- `-i, --ip` : Target IP address.
- `-s, --start` : Starting port (default: 1).
- `-e, --end` : Ending port (default: 500).
- `-t, --threads` : Number of threads to use (default: 500).
- `-v, --verbose` : Enable verbose output.

#### 📌 Example:
```sh
python port_sniff.py -m scan -i 192.168.1.2 -s 20 -e 1000 -t 300 -v
```

### 🕵️‍♂️ Packet Sniffing Mode
To sniff HTTP traffic on a network interface:

```sh
python port_sniff.py -m sniff -i <NETWORK_INTERFACE>
```

#### 📌 Example:
```sh
python port_sniff.py -m sniff -i eth0
```

## ⚠️ Notes
Ensure you have proper authorization before scanning any network.  
The tool is designed for ethical hacking, penetration testing, and network security research.  
  


## ⚠️ Disclaimer
The developers take no responsibility for misuse of this tool. Use it only in legal and ethical scenarios.


