from __future__ import print_function
try:
    from googlesearch import search
    from colorama import Fore,Style
    import os


except ImportError:
    print("")

import sys
import time





if sys.version[0] in "2":
    print ("\n[x] ..n00b.. Dork Harvest Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tDork Harvest \033[1;94mI like to See Ya, Hacking \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

os.system("clear")
banner = (f"""
    {Fore.WHITE}                       ███████████████████████████
                           ███████▀▀▀░░░░░░░▀▀▀███████
                           ████▀░░░░░░░░░░░░░░░░░▀████
                           ███│░░░░░░░░░░░░░░░░░░░│███
                           ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                           ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                           ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                           ██░░┌┘{Fore.BLUE}▄▄▄▄▄{Fore.WHITE}░░░░{Fore.BLUE}░▄▄▄▄▄{Fore.WHITE}└┐░░██
                           ██▌░|{Fore.BLUE}██████▌{Fore.WHITE}░░░{Fore.BLUE}▐██████{Fore.WHITE}│░▐██
                           ███░│{Fore.BLUE}▐███▀▀{Fore.WHITE}░░{Fore.BLUE}▄{Fore.WHITE}░░{Fore.BLUE}▀▀███▌{Fore.WHITE}│░███
                           ██▀─┘░░░░░░░{Fore.BLUE}▐█▌{Fore.WHITE}░░░░░░░└─▀██
                           ██▄░░░{Fore.BLUE}▄▄▄▓{Fore.WHITE}░░{Fore.BLUE}▀█▀{Fore.WHITE}░░{Fore.BLUE}▓▄▄▄{Fore.WHITE}░░░▄██
                           ████▄─┘{Fore.BLUE}██▌{Fore.WHITE}░░░░░░░{Fore.BLUE}▐██{Fore.WHITE}└─▄████
                           █████░░{Fore.BLUE}▐█─┬┬┬┬┬┬┬─█▌{Fore.WHITE}░░█████
                           ████▌░░░{Fore.BLUE}▀┬┼┼┼┼┼┼┼┬▀{Fore.WHITE}░░░▐████
                           █████▄░░░{Fore.BLUE}└┴┴┴┴┴┴┴┘{Fore.WHITE}░░░▄█████
                           ███████▄░░░░░░░░░░░▄███████ {Fore.RED}
┌─[✗{Fore.WHITE}]─[{Fore.GREEN}root{Fore.YELLOW}@{Fore.CYAN}parrot-dev{Fore.RED}]─[{Fore.GREEN}~{Fore.RED}]{Fore.WHITE}██████████▄▄▄▄▄▄▄██████████{Fore.RED}
└──╼ {Fore.YELLOW}$ {Fore.RED}THE HARVESTERS      {Fore.WHITE}███████████████████████████ 

  {Fore.WHITE}      ██████████████████████████████████████████████████████████████████
  {Fore.BLUE}      █▄─▄▄▀█─▄▄─█▄─▄▄▀█▄─█─▄███─█─██▀▄─██▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄▄▄▄█─▄─▄─█
        ██─██─█─██─██─▄─▄██─▄▀████─▄─██─▀─███─▄─▄██▄▀▄███─▄█▀█▄▄▄▄─███─███
  {Fore.WHITE}      ▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀ """)


for col in banner:
    print(col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
 """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = f"\n\t\t       What would you like to search for{Fore.YELLOW}?\n"
for col in y:
    print(col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input(f"\n{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Would You Like To Save The Output In A File{Fore.YELLOW}? {Fore.RED}({Fore.CYAN}Y{Fore.RED}/{Fore.CYAN}n{Fore.RED}) {Fore.WHITE}").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print (f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.RED} User Interruption Detected {Fore.WHITE}!")
        time.sleep(0.5)
        print (f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.GREEN} Task has completed successfully... ") 
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    with open(f"{l0g}.txt", "a") as file:
        file.write(str(data))
        file.write("\n")


if data.startswith("y" or "Y"):
    l0g = input(f"{Fore.red}[~] {Fore.green}Enter a file name: {Fore.WHITE} ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print (f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.BLUE}Saving is Skipped{Fore.WHITE}...")
    print ("\n" + "  " + f"{Fore.RED}»" * 78 + "\n")


def dorks():
    try:
        dork = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Enter The Dork Search Query{Fore.YELLOW}:{Fore.WHITE} ")
        amount = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Enter The Number Of Websites To Display{Fore.YELLOW}:{Fore.WHITE} ")
        print (f"\n{Fore.BLUE} ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] Task has completed successfully \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print (f"{Fore.RED}Dork Harvest")
    print (f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Task has completed successfully")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
