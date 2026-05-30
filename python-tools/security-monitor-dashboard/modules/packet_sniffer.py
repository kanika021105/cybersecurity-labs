from scapy.all import sniff

def capture_packet():

    packets = sniff(count=1)

    for packet in packets:

        if packet.haslayer("IP"):

            return {
                "src": packet["IP"].src,
                "dst": packet["IP"].dst,
                "proto": packet["IP"].proto
            }

    return None
