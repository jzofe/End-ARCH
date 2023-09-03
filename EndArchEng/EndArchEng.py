 
import os
import subprocess
import time
import sys
import getpass
from colorama import Fore, Style, init

# CODER FYKS

# THIS PROGRAM IS MADE EXCLUSIVELY FOR THE ENDER COMMUNITY. IT IS DISTRIBUTED FOR FREE AND OPEN-SOURCE.
# THERE IS NO OBJECTION TO MODIFYING THE CODE AND DISTRIBUTING IT ON GITHUB-LIKE PLATFORMS. YOU CAN GIVE CREDIT TO CONTRIBUTE TO THE DEVELOPMENT OF THE ENDER COMMUNITY.
# FOR MORE INFORMATION, YOU CAN CONTACT US.

# ENDER COMMUNITY DISCORD: https://discord.gg/z9yQfFXk
# ENDER COMMUNITY PATREON: https://www.patreon.com/EnderProject
# ENDER COMMUNITY WEBSITE: https://endertopluluk.com

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


def waiting_animation(message):
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.2)
        sys.stdout.write("\r" + message + animation[i % len(animation)])
        sys.stdout.flush()


def module_check(module_name):
    result = run_command(f"pacman -Q {module_name}")
    if result.returncode == 0:
        print(f"Modules are being downloaded... Please wait.")
        time.sleep(1)
        print(Fore.GREEN + "[+]" + Style.RESET_ALL + " Modules are already downloaded. You are being redirected.")
        time.sleep(2)
    else:
        print(f"Modules are being downloaded... Please wait.")
        time.sleep(2)
        print(Fore.GREEN + "[+]" + Style.RESET_ALL + " Modules are successfully downloaded. You are being redirected.")
        time.sleep(3)


def main():
    if os.geteuid() != 0:
        print(Fore.RED + "[!]" + Style.RESET_ALL + " You can only run this script as root. | End Arch")
        return

    module_name = "macchanger"
    module_check(module_name)
    clear_screen()

    while True:
        print_header()
        print(f"{Fore.LIGHTBLACK_EX}Arch-Linux commands | EndArch{Style.RESET_ALL}")

        print(f"{Fore.CYAN}#{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Update System")
        print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Tools")
        print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}3{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Network Manager")
        print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}4{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Random MAC Address")
        print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}5{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Change MAC Address")
        print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}6{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Exit")

        selection = input(f"{Fore.LIGHTBLACK_EX}Enter your selection: {Style.RESET_ALL}")

        if selection == '1':
            print("Updating system...")
            result = run_as_root("pacman -Syu --noconfirm")
            if result:
                print(Fore.GREEN + "[+]" + Style.RESET_ALL + " System is up to date.")
                waiting_animation("Restarting your computer... ")
                run_as_root("reboot")
            else:
                print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to update the system.")
        elif selection == '2':
            while True:
                clear_screen()
                print_header()
                print(f"{Fore.LIGHTBLACK_EX}Tools | EndArch{Style.RESET_ALL}")

                print(f"{Fore.CYAN}#{Style.RESET_ALL}")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Install Package")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Remove Package")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}3{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Install AUR Package")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}4{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Remove AUR Package")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}5{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} List Installed Packages")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}6{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Back to Main Menu")

                selection = input(f"{Fore.LIGHTBLACK_EX}Enter your selection: {Style.RESET_ALL}")

                if selection == '1':
                    package = input("Enter the name of the package to install: ")
                    result = run_as_root(f"pacman -S --noconfirm {package}")
                    if result:
                        print(Fore.GREEN + "[+]" + Style.RESET_ALL + f" {package} has been successfully installed.")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + f" Failed to install {package}.")
                elif selection == '2':
                    package = input("Enter the name of the package to remove: ")
                    result = run_as_root(f"pacman -R --noconfirm {package}")
                    if result:
                        print(Fore.GREEN + "[+]" + Style.RESET_ALL + f" {package} has been successfully removed.")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + f" Failed to remove {package}.")
                elif selection == '3':
                    package = input("Enter the name of the AUR package to install: ")
                    result = run_command(f"git clone https://aur.archlinux.org/{package}.git")
                    if result.returncode == 0:
                        package_dir = package.split('/')[-1].split('.')[0]
                        os.chdir(package_dir)
                        result = run_command("makepkg -si --noconfirm")
                        if result.returncode == 0:
                            print(Fore.GREEN + "[+]" + Style.RESET_ALL +
                                  f" {package} has been successfully installed.")
                        else:
                            print(Fore.RED + "[-]" + Style.RESET_ALL +
                                  f" Failed to install {package}.")
                        os.chdir("..")
                        run_command(f"rm -rf {package_dir}")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL +
                              f" Failed to download {package}.")
                elif selection == '4':
                    package = input("Enter the name of the AUR package to remove: ")
                    result = run_command(f"git clone https://aur.archlinux.org/{package}.git")
                    if result.returncode == 0:
                        package_dir = package.split('/')[-1].split('.')[0]
                        os.chdir(package_dir)
                        result = run_command("makepkg -si --noconfirm")
                        if result.returncode == 0:
                            print(Fore.GREEN + "[+]" + Style.RESET_ALL +
                                  f" {package} has been successfully removed.")
                        else:
                            print(Fore.RED + "[-]" + Style.RESET_ALL +
                                  f" Failed to remove {package}.")
                        os.chdir("..")
                        run_command(f"rm -rf {package_dir}")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL +
                              f" Failed to download {package}.")
                elif selection == '5':
                    result = run_command("pacman -Q")
                    if result.returncode == 0:
                        print(result.stdout)
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to list installed packages.")
                elif selection == '6':
                    break
                else:
                    print(Fore.RED + "[-]" + Style.RESET_ALL + " Invalid selection. Please try again.")
                input("Press Enter to continue...")
        elif selection == '3':
            while True:
                clear_screen()
                print_header()
                print(f"{Fore.LIGHTBLACK_EX}Network Manager | EndArch{Style.RESET_ALL}")

                print(f"{Fore.CYAN}#{Style.RESET_ALL}")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}1{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Start Network Manager")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}2{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Stop Network Manager")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}3{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Restart Network Manager")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}4{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Show Network Connections")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}5{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Connect to a Network")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}6{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Disconnect from a Network")
                print(f"{Fore.BLUE}[{Style.RESET_ALL}{Fore.GREEN}7{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL} Back to Main Menu")

                selection = input(f"{Fore.LIGHTBLACK_EX}Enter your selection: {Style.RESET_ALL}")

                if selection == '1':
                    result = run_as_root("systemctl start NetworkManager")
                    if result:
                        print(Fore.GREEN + "[+]" + Style.RESET_ALL + " Network Manager started successfully.")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to start Network Manager.")
                elif selection == '2':
                    result = run_as_root("systemctl stop NetworkManager")
                    if result:
                        print(Fore.GREEN + "[+]" + Style.RESET_ALL + " Network Manager stopped successfully.")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to stop Network Manager.")
                elif selection == '3':
                    result = run_as_root("systemctl restart NetworkManager")
                    if result:
                        print(Fore.GREEN + "[+]" + Style.RESET_ALL + " Network Manager restarted successfully.")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to restart Network Manager.")
                elif selection == '4':
                    result = run_command("nmcli connection show")
                    if result.returncode == 0:
                        print(result.stdout)
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to show network connections.")
                elif selection == '5':
                    ssid = input("Enter the SSID of the network to connect to: ")
                    password = input("Enter the password for the network (leave empty for open networks): ")
                    if password:
                        result = run_command(f"nmcli device wifi connect '{ssid}' password '{password}'")
                    else:
                        result = run_command(f"nmcli device wifi connect '{ssid}'")
                    if result.returncode == 0:
                        print(Fore.GREEN + "[+]" + Style.RESET_ALL + f" Connected to {ssid}.")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + f" Failed to connect to {ssid}.")
                elif selection == '6':
                    result = run_command("nmcli device disconnect")
                    if result.returncode == 0:
                        print(Fore.GREEN + "[+]" + Style.RESET_ALL + " Disconnected from the network.")
                    else:
                        print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to disconnect from the network.")
                elif selection == '7':
                    break
                else:
                    print(Fore.RED + "[-]" + Style.RESET_ALL + " Invalid selection. Please try again.")
                input("Press Enter to continue...")
        elif selection == '4':
            mac_address = generate_random_mac_address()
            result = change_mac_address(interface, mac_address)
            if result:
                print(Fore.GREEN + "[+]" + Style.RESET_ALL + f" MAC address of {interface} changed to {mac_address}.")
            else:
                print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to change MAC address.")
        elif selection == '5':
            new_mac = input("Enter the new MAC address (format: XX:XX:XX:XX:XX:XX): ")
            result = change_mac_address(interface, new_mac)
            if result:
                print(Fore.GREEN + "[+]" + Style.RESET_ALL + f" MAC address of {interface} changed to {new_mac}.")
            else:
                print(Fore.RED + "[-]" + Style.RESET_ALL + " Failed to change MAC address.")
        elif selection == '6':
            print("Exiting EndArch...")
            sys.exit(0)
        else:
            print(Fore.RED + "[-]" + Style.RESET_ALL + " Invalid selection. Please try again.")
