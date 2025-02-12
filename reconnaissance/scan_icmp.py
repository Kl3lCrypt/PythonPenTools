#!/usr/bin/env python3

import subprocess
import argparse
from termcolor import colored
import sys
import signal
from concurrent.futures import ThreadPoolExecutor


def def_handler(sig, frame):
    print(colored(f"[!] Saliendo del programa...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para descubrir hosts activos en una red (ICMP)")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")
    args = parser.parse_args()
    return args.target

def parse_target(target_str):

    target_str_splitted = target_str.split('.')
    first_three_octets = ".".join(target_str_splitted[:3])

    if len(target_str_splitted) == 4:
        if "-" in target_str_splitted[3]:
            start, end = target_str_splitted[3].split("-")
            return [f"{first_three_octets}.{i}" for i in range(int(start),int(end)+1)]
        else:
            return [target_str]
    else:
        print(colored(f"\n[!] Formato de IP Invalido", "red"))
        sys.exit(2)

def host_discovery(target):

    try:
        ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
        if ping.returncode == 0:
            print(colored(f"[+] La IP {target} esta ACTIVA", "green"))
    except subprocess.TimeoutExpired:
        pass




def main():

    target_str = get_arguments()
    targets = parse_target(target_str)

    print(colored(f"\n[+] Host activos en la red:\n", "green"))

    max_threads = 100

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_discovery, targets)


if __name__ == "__main__":
    main()
