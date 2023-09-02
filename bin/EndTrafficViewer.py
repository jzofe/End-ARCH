import socket
import struct
from colorama import Fore, Style, init
import sys

sys.stdout = sys.stderr = open('/dev/tty', 'w')

# Bu tool Endertopluluğa özel yapılmıştır
print("EndTrafficViewer çalıştı. Bu tool, ağınızdaki gelen ve giden paketlerin MAC adreslerini görüntülemenizi sağlayacaktır.")
print(f"{Fore.RED}Eğer ağ biriminizi bilmiyorsanız 'ifconfig' komudu ile öğrenebilirsiniz.{Style.RESET_ALL}")
agbirimi = input(f"{Fore.GREEN} Lütfen ağ arabirimi adını girin (örneğin, eth0):{Style.RESET_ALL} ")

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

        print(f"{Fore.GREEN}Hedef MAC adresi: {dest_mac.hex()} Kaynak MAC adresi: {src_mac.hex()}{Style.RESET_ALL}")

except OSError as e:
    print(f"{Fore.RED}Hata: {e}{Style.RESET_ALL}")
