import socket
import struct
from colorama import Fore, Style, init
import sys, os

sys.stdout = sys.stderr = open('/dev/tty', 'w')

GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

# Bu tool Endertopluluğa özel yapılmıştır
os.system('clear')
print(" - EndTrafficViewer, ağınızdaki gelen ve giden paketlerin MAC adreslerini görüntülemenizi sağlayacaktır")
print("")

agbirimi = input(f"{BLUE} >> {RED}Lütfen ağ arabirimi adını girin (örneğin, eth0):{RESET} ")

try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    s.bind((agbirimi, 0))

    while True:
        packet = s.recvfrom(65565)
        packet = packet[0]
        eth_length = 14

        eth_header = packet[:eth_length]
        eth = struct.unpack("!6s6sH", eth_header)

        dest_mac = eth[0]
        src_mac = eth[1]

        print(f"{GREEN}> Hedef MAC adresi: {RESET} {WHITE} {dest_mac.hex()}{RESET}  {GREEN} | > Kaynak MAC adresi: {RESET} {WHITE} {src_mac.hex()}{RESET} {RESET} |{RED} Ağ birimi : {agbirimi}{RESET}")

except OSError as e:
    print(f"{RED}Hata: {e}{RESET}")
