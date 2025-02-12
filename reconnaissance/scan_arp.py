#!/usr/bin/env pyhton3

import argparse
import scapy.all as scapy


def get_arguments():
    parser = argparse.ArgumentParser(description="Escaner para detectar host activo mediante ARP")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP range")

    args = parser.parse_args()
    return args.target


def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_packet = broadcast_packet/arp_packet

    answared, unanswared = scapy.srp(arp_packet, timeout=1, verbose=False)

    response = answared.summary()

    if response:
        print(response)

def main():
    target = get_arguments()
    scan(target)

if __name__ == '__main__':
    main()
