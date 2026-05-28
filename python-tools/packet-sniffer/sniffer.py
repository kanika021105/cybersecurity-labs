from scapy.all import sniff


def packet_callback(packet):

    print("\nPacket Captured")

    if packet.haslayer("IP"):

        print(f"Source IP: {packet['IP'].src}")
        print(f"Destination IP: {packet['IP'].dst}")
        print(f"Protocol: {packet['IP'].proto}")


sniff(prn=packet_callback, count=5)
