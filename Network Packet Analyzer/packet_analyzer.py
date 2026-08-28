from scapy.all import sniff, IP, TCP, UDP, ICMP

# Packet count
packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1
    
    print(f"\n--- Packet #{packet_count} ---")

    # IP layer unte
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

        # Protocol check
        if TCP in packet:
            print(f"Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport} -> Dest Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport} -> Dest Port: {packet[UDP].dport}")
        elif ICMP in packet:
            print(f"Protocol: ICMP")
        else:
            print(f"Protocol: Other - {packet[IP].proto}")

        # Payload size
        if packet[IP].payload:
            payload_len = len(packet[IP].payload)
            print(f"Payload Size: {payload_len} bytes")
            
            # First few bytes of data chupinchadam (optional)
            try:
                data = bytes(packet[IP].payload)[:30]
                print(f"Data (sample): {data}")
            except:
                pass
    else:
        print("Non-IP Packet")
        print(packet.summary())

print("=== Network Packet Analyzer Started ===")
print("Packets ni capture chesthunna... Stop cheyali ante CTRL+C kotu")
print("Admin ga run chesthunav kada?")

# Main sniffing - 10 packets matrame capture chestundi
# count=0 pedithe infinite ga capture chestundi
try:
    sniff(prn=analyze_packet, count=15, store=False)
except PermissionError:
    print("\nERROR: Admin / Sudo permission tho run cheyali!")
except KeyboardInterrupt:
    print("\n\nSniffing stopped by you.")

print(f"\nTotal {packet_count} packets captured. Task complete!")