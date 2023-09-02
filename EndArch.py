
import os
import subprocess
import time
from colorama import Fore, Style, init
# CODER FYKS

# BU PROGRAM TAMAMEN ENDER TOPLULUK İÇİN YAPILMIŞTIR. ÜCRETSİZ VE OPEN-SOURCE DAĞITILMIŞTIR
# KODLARIN DEĞİŞTİRİLİP GITHUB BENZERİ PLATFORMLARDA DAĞITILMASINDA HİÇBİR SAKINCA YOKTUR, ENDER TOPLULUĞUN GELİŞMESİNDE BÜYÜK KATKITA BULUNMAK İÇİN CREDIT VEREBİLİRSİNİZ.
# DAHA FAZLA BİLGİ İÇİN BİZE ULAŞABİLİRSİNİZ.

# ENDER TOPLULUK DİSCORD : https://discord.gg/z9yQfFXk
# ENDER TOPLULUK PATREON : https://www.patreon.com/EnderProject
# ENDER TOPLULUK WEBSITESİ : https://endertopluluk.com

os.system('clear')
init(autoreset=True)


def clear_screen():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


def run_command(command):
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result


def run_command_silent(command):
    result = subprocess.run(
        command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)
    return result.returncode


def print_header():
    header = r"""
    ▓█████  ███▄    █ ▓█████▄     ▄▄▄       ██▀███   ▄████▄   ██░ ██
    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌   ▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
    ▒███   ▓██  ▀█ ██▒░██   █▌   ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌   ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██
    ░▒████▒▒██░   ▓██░░▒████▓     ▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒     ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
      ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒      ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
        ░      ░   ░ ░  ░ ░  ░      ░   ▒     ░░   ░ ░         ░  ░░ ░
        ░  ░         ░    ░             ░  ░   ░     ░ ░       ░  ░  ░
                       ░                            ░
    """
    print(Fore.GREEN + header + Style.RESET_ALL)


def run_as_root(command):
    try:
        result = subprocess.run(
            f"sudo {command}", shell=True, check=True, stdout=subprocess.PIPE, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False


def check_module_installed(module_name):
    result = run_command(f"pacman -Q {module_name}")
    if result.returncode == 0:
        print(f"Modüller indiriliyor... Lütfen bekleyiniz")
        time.sleep(1)
        print(f"Modüller zaten indirilmiş. Yönlendiriliyorsunuz")
        time.sleep(2)
    else:
        print(f"Modüller indiriliyor... Lütfen bekleyiniz")
        time.sleep(2)
        print(f"Modüller başarıyla indirildi. Yönlendiriliyorsunuz")
        time.sleep(3)


def main():
    if os.geteuid() != 0:
        print("Bu scripti sadece root olarak çalıştırabilirsiniz. | End Arch")
        return

    module_name = "macchanger"
    check_module_installed(module_name)
    clear_screen()

    while True:
        print_header()
        print(
            f"{Fore.LIGHTBLACK_EX}              Arch-Linux komutları | EndArch{Style.RESET_ALL}")

        print(f"{Fore.CYAN}#{Style.RESET_ALL}")
        print(
            f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Sistemi Güncelle")
        print(
            f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Toollar")
        print(
            f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}3{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Ekstra araçlar")
        print(
            f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}4{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Bilgi")
        print(
            f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}5{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Çık")

        print(
            f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}6{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Arch Sorun giderici")
        print(
            f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}7{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} >>EnderTopluluk Web sitesi<<")

        choice = input("Lütfen bir seçenek seçin : ")

        if choice == '1':
            result = run_command_silent("sudo pacman -Syu --noconfirm")
            if result == 0:
                print("Sistem güncellendi.")
            else:
                print("Sistem güncelleme sırasında bir hata oluştu.")
        elif choice == '4':
            while True:
                clear_screen()
                print(
                    f"{Fore.LIGHTBLACK_EX}              Arch Bilgi ve Destek | EndArch{Style.RESET_ALL}")
                print("Hoş geldiniz Arch kullanıcıları! End Arch, Arch Linux işletim sistemi için geliştirilmiş açık kaynak ve ücretsiz bir Ender topluluk projesidir.")
                print("End Arch, aşağıdaki özellikleri sunar:")
                print(
                    "- Sisteminizi güncelleyebilir ve temel işlemleri gerçekleştirebilirsiniz.")
                print(
                    "- Arch sorun giderici aracımızı kullanarak işletim sisteminizdeki sorunları çözebilirsiniz.")
                print(
                    "- Mac adresinizi değiştirebilir, EndMacchanger ile otomatik olarak güncelleyebilirsiniz.")
                print(
                    "- Otomatik openVPN hizmeti ile güvenli bir şekilde internete bağlanabilirsiniz.")
                print(
                    "- Ağınızdaki gelen ve giden paketleri incelemek için EndTrafficViewer kullanabilirsiniz.")
                print(
                    "- Donanım kimliğinizi gizlemek için HWID spoofing yapabilirsiniz.")
                print("- BlackArch toolarını otomatik olarak kurabilirsiniz.")
                print("- BeefHack ile güvenlik testleri yapabilirsiniz.")
                print(
                    "End Arch'i kullanarak, Arch Linux işletim sisteminizi daha güvenli ve işlevsel hale getirebilirsiniz.")
                print(
                    f"{Fore.BLUE}Discord : https://discord.gg/z9yQfFXk {Style.RESET_ALL}")
                print(
                    f"{Fore.BLUE}Patreon : https://www.patreon.com/EnderProject {Style.RESET_ALL}")
                print(">>Coder Fyks<<")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Devam et")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Geri dön")
                sub_choice = input("Lütfen bir seçenek seçin : ")
                if sub_choice == '1':
                    break
                elif sub_choice == '2':
                    clear_screen()
                    break
                else:
                    input("Geçersiz seçenek. Devam etmek için Enter'a basın.")
        elif choice == '2':
            while True:
                print_header()
                clear_screen()
                print(
                    f"{Fore.LIGHTBLACK_EX}              Toollar | EndArch{Style.RESET_ALL}")
                print(f"{Fore.CYAN}#{Style.RESET_ALL}")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Mac Adresimi Değiştir                   {Fore.YELLOW}[{Style.RESET_ALL}{Fore.YELLOW}8{Style.RESET_ALL}{Fore.YELLOW}]{Style.RESET_ALL}{Fore.YELLOW} End Botnet")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} EndMacchanger (Loop)                   {Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}9{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Metasploit+Msfconsole (Otomatik kurulum)") 
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}3{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} VPN            {Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}10{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} End Cloudflare Bypass")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}4{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} EndTrafficViewer")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}5{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} HWID spoofer                   {Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}11{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} End DdoS script")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}6{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Blackarch (Otomatik kurulum)")

                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}7{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} BeefHack                   {Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}12{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} >>EnderTopluluk Web sitesi<<")

                sub_choice = input(" Lütfen bir seçenek seçin : ")

                if sub_choice == '1':
                    print("Macchanger scripti çalıştırılıyor...")
                    time.sleep(3)
                    clear_screen()
                    interface = input(
                        f"{Fore.GREEN}  Arayüz adını girin (örn. wlan0) : ")
                    result = run_command_silent(
                        f"sudo macchanger -R {interface}")
                    if "New MAC" in result.stdout:
                        print("Mac adresiniz değiştirildi.")
                    else:
                        print("Mac adresiniz değiştirilemedi.")
                elif sub_choice == '2':
                    print("EndMacchanger scripti çalıştırılıyor... ")
                    time.sleep(3)
                    clear_screen()
                    arayuz = input(
                        f"{Fore.GREEN}  Arayüz adını girin (örn. wlan0) : ")
                    sure = int(input(
                        f"{Fore.GREEN}  Kaç saniye içinde tekrar mac adresinizin değiştirilmesini istiyorsunuz? (örn. 150):{Style.RESET_ALL} "))
                    print(
                        f"{Fore.RED}EndMacchanger çalışıyor. MAC adresiniz her {sure} saniyede bir değiştirilecek.{Style.RESET_ALL}")
                    run_command_silent(
                        f"sudo watch -n {sure} macchanger -r {arayuz}")
                    time.sleep(5)
                    print(f"{Fore.RED}MAC adresiniz değiştirildi.{Style.RESET_ALL}")
                    time.sleep(sure)
                    print(f"{Fore.RED}MAC adresiniz değiştirildi.{Style.RESET_ALL}")
                elif sub_choice == '6':
                    clear_screen()
                    print(
                        "BlackArch toolarını kuruluyor... Bu işlem biraz zaman alabilir. ")
                    run_command("curl -O https://blackarch.org/strap.sh")
                    run_command(
                        "echo 5ea40d49ecd14c2e024deecf90605426db97ea0c strap.sh | sha1sum -c")
                    run_command("chmod +x strap.sh")
                    run_command("sudo ./strap.sh")
                    run_command("sudo pacman -Syu --noconfirm")
                    print(
                        "BlackArch tooları başarıyla kuruldu ! Toolları görüntülemek için, 'sudo pacman -S blackarch'")
                    time.sleep(10)
                    clear_screen()
                elif sub_choice == '8':
                    print("End Botnet ağına sahip olmak istiyorsanız websitemizden bize ulaşıp ücretli bir şekilde temin edebilirsiniz, https://endertopluluk.com ")

                elif sub_choice == '9':
                    print("Otomatik Metasploit kurulumu başladı... Bu işlem zaman alabilir")
                    time.sleep(2)
                    run_command_silent("sudo pacman -S metasploit --noconfirm ")
                    run_command_silent("")
                    time.sleep(1)
                    print("Metasploit kurulumu tamamlandı!")

                    input("Ana menüye dönmek için Enter'a basın...")
                elif sub_choice == '7':
                    print("beEF toolu indirme işlemi başladı...")
                    time.sleep(1)
                    run_command_silent("git clone https://github.com/beefproject/beef")
                    run_command_silent("cd beef & sudo ./install")
                    run_command_silent("cd ..")
                    print("beEF toolu kurulumu ve indirme işlemi tamamlandı. Tool, beef klasörüne gidip ./beef yazarsanız çalışacaktır.")
                

                elif sub_choice == '4':
                        clear_screen()
                        print("EndTrafficViewer başlatılıyor...")
                        time.sleep(2)
                        clear_screen()
                        betik_yolu = os.path.expanduser("/home/fyks/Desktop/EndArch/bin/EndTrafficViewer.py")
                        process = subprocess.Popen(['sudo', 'python', betik_yolu], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        while True:
                            output = process.stdout.readline()
                            if output == '' and process.poll() is not None:
                                break
                            if output:
                                print(output.strip())

                        while True:
                            error_output = process.stderr.readline()
                            if error_output == '' and process.poll() is not None:
                                break
                            if error_output:
                                print("Hata mesajı:")
                                print(error_output.strip())
                                

              

           
        elif choice == '6':
            while True:
                print_header()
                clear_screen()
                print(
                    f"{Fore.LIGHTBLACK_EX}              Arch sorun giderici | EndArch{Style.RESET_ALL}")
                print("Bu özellik, yalnızca ARCH Linux işletim sistemi üzerinde belirli sorunlara çözüm sunmak amacıyla oluşturulmuştur. Eğer bu sorunları yaşamıyorsanız bu özelliği KULLANMAYIN!.")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Çözünürlük sorunlarını çöz (Xrandr)")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Bluetooth sorunlarını çöz (Bluez)")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}3{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} İnternet sorunlarını çöz")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}4{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Wine sorunlarını çöz")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}5{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Önerilen pacman paketlerini kur")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}6{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Diğer sorunlar")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}7{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Geri dön")
                sub_choice = input("Lütfen bir seçenek seçin : ")

            if sub_choice == '1':
                clear_screen()
                ekranadi = input(
                    "Çözünürlük sorunu yaşadığınız ekranın adını giriniz (örn. VGA-1): ")
                cozunurluk = input(
                    f"{Fore.GREEN} Ekrana zorunlu olarak uygulanacak çözünürlük (örn. 1920x1080)  :  ")
                herz = input(
                    f"{Fore.GREEN} Çözünürlüğü herzleriyle birlikte belirtin (örn. 1920 1080 144): ")
                command = f"""xrandr --newmode $(cvt {herz} | grep Mode | sed -e 's/.*"/{cozunurluk}/')"""
                result = run_command_silent(command)

                if result == 0:
                    run_command_silent(
                        f"xrandr --addmode {ekranadi} {cozunurluk}")
                    run_command_silent(
                        f"xrandr --output {ekranadi} --mode '{cozunurluk}' ")
                    print("Çözünürlük uygulandı.")
                else:
                    print("Çözünürlük uygulanamadı.")
            elif sub_choice == '2':
                clear_screen()
                print("Bluetooth sorunları çözülüyor... ")
                run_command("systemctl enable bluetooth.service")
                run_command("systemctl start bluetooth.service")
                print(f"Bluetooth sorunları çözüldü.")
            elif sub_choice == '4':
                clear_screen()
                print("Wine ile ilgili sorunlar çözülüyor...")
                time.sleep(2)
                run_command_silent("sudo pacman -R wine")
                run_command_silent("sudo pacman -S wine")
                run_command_silent("ulimit -s unlimited")
                print(
                    f"Başarılı. Hâlâ sorunlar çözülmediyse Wine'yi root olarak çalıştırmayı deneyebiliriz")
                wine = input(
                    f"{Fore.GREEN}Çalıştırmak istediğiniz programın adını girin :{Style.RESET_ALL}")
                run_command_silent(f"sudo wine {wine} ")
            elif sub_choice == '5':
                run_command(
                    "sudo pacman -Syu --needed --noconfirm $(pacman -Qq | grep -v \"$(pacman -Qqe)\")")
            elif sub_choice == '6':
                print("Diğer sorunların çözümü için : https://discord.gg/z9yQfFXk")
            elif sub_choice == '7':
                clear_screen()
                break
            else:
                input("Geçersiz seçenek. Devam etmek için Enter'a basın.")
        elif choice == '3':
            while True:
                print_header()
                clear_screen()
                print(
                    f"{Fore.LIGHTBLACK_EX}              Ekstra araçlar | EndArch{Style.RESET_ALL}")
                print(f"{Fore.CYAN}#{Style.RESET_ALL}")
                print(f"{Fore.CYAN}#{Style.RESET_ALL}")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Timeshift (yedekleme ve geri yükleme aracı)")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.RED}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Pacman/pamac/yay/AUR üzerinden paket indirme işlemi")
                print(
                    f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}8{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} >>EnderTopluluk Web sitesi<<")

                sub_choice = input("Lütfen bir seçenek seçin : ")
                if sub_choice == '2':
                    clear_screen()
                    print(
                        f"Bu seçenek istediğiniz bir uygulamayı bir çok packet managerde arayarak indirecektir.")
                    time.sleep(3)
                    packetx = input(f"İndirmek istediğiniz uygulama : ")
                    run_command_silent("sudo pacman -S {packetx} --noconfirm")
                    run_command_silent("sudo pamac install {packetx} ")
                    run_command_silent("sudo yay -S {packetx} --noconfirm")
                    run_command_silent(
                        "git clone https://aur.archlinux.org/{packetx}.git")
                    print(
                        "{packetx} uygulamasını Pacman, pamac, yay ve aur üzerinden indirmeyi denedik. Kurulup kurulmadığına bakabilirsiniz.")
                elif sub_choice == '1':
                    clear_screen()
                    print("Timeshift yedekleme ve geri yükleme aracı kuruluyor... ")
                    run_command("sudo pacman -S timeshift")
                    print("Timeshift başarıyla kuruldu.")
                elif sub_choice == '8':
                    break
                else:
                    input("Geçersiz seçenek. Devam etmek için Enter'a basın.")
        elif choice == '5':
            clear_screen()
            print("EndArch'tan çıkılıyor... İyi günler dileriz!")
            break
        elif choice == '7':
            clear_screen()
            print("Ender Topluluk Web Sitesine yönlendiriliyorsunuz... ")
            time.sleep(3)
            os.system("xdg-open https://endertopluluk.com")
        else:
            input("Geçersiz seçenek. Devam etmek için Enter'a basın.")

if __name__ == "__main__":
    main()
