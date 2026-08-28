# Task-05: Network Packet Analyzer (Packet Sniffer)

## 📌 Description
Develop a packet sniffer tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.

> ⚠️ **ETHICAL DISCLAIMER:** This tool is for educational use only. Use it only on your own network / with explicit permission. Sniffing others' traffic without consent is illegal.

## 🌐 What is a Packet Sniffer?
A packet sniffer intercepts and logs network traffic. It helps in understanding how data flows over a network, debugging, and learning network protocols.

## ✨ Features
- Captures live network packets
- Shows Source IP, Destination IP
- Shows Protocol (TCP, UDP, ICMP)
- Shows Source/Destination Ports
- Displays payload data (in hex / text)
- Save logs to file

## ⚙️ How It Works
1. Uses `scapy` to sniff packets from network interface
2. Parses Ethernet -> IP -> TCP/UDP headers
3. Extracts and displays useful info
4. Logs to console and file

## 🚀 How to Run

```bash
pip install scapy
python packet_sniffer.pyNote: Run as Administrator / sudo:bashsudo python packet_sniffer.py  # Linux/Mac
# Windows: Run CMD as Administrator💻 Example OutputjavascriptPacket #1:
Source IP: 192.168.1.5 -> Destination IP: 142.250.195.78
Protocol: TCP | Src Port: 54321 -> Dst Port: 443
Payload: 120 bytes

Packet #2:
Source IP: 192.168.1.5 -> Destination IP: 8.8.8.8
Protocol: UDP | Src Port: 5353 -> Dst Port: 53🛠️ Tech Stack
Python 3.xScapy librarySocket📁 File Structure
Task-05/
├── packet_sniffer.py
├── capture_log.txt
└── README.md
⚠️ Ethical Use
Test only on your own WiFi / lab networkDon't capture sensitive data of othersFor Prodigy Infotech internship learning only
