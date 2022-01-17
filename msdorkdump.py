from colorama import Fore, Style, init
import urllib.request
import time
import sys
import os
from os.path import exists
from googlesearch import search
import random
global domain

global success, info, fail
success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT
global file_types
file_types = ['doc', 'docx', 'ppt', 'pptx', 'csv', 'pdf', 'xls', 'xlsx']


def banner():
    styles = [Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX,
              Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX]
    random_index = random.randint(0, len(styles)-1)
    print(styles[random_index] + "")
    print('██████╗  ██████╗ ██████╗ ██╗  ██╗  ██████╗ ██╗   ██╗███╗   ███╗██████╗ ')
    print('██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝  ██╔══██╗██║   ██║████╗ ████║██╔══██╗')
    print('██║  ██║██║   ██║██████╔╝█████╔╝   ██║  ██║██║   ██║██╔████╔██║██████╔╝')
    print('██║  ██║██║   ██║██╔══██╗██╔═██╗   ██║  ██║██║   ██║██║╚██╔╝██║██╔═══╝ ')
    print('██████╔╝╚██████╔╝██║  ██║██║  ██╗  ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     ')
    print('╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝   \n')
    print('                       Google Dork File Finder                         ')
    print('                            Version 1.0.0                              ')
    print('                       A project by The Mayor                          ')
    print('               python3 msdorkdump.py <domain> to start                 ' + Style.RESET_ALL)
    print("-" * 73)


def msdorker():
    request = 0
    try:
        path = domain
        isdir = os.path.isdir(path)
        if isdir is True:
            pass
        else:
            os.mkdir(domain)        
        for files in file_types:
            print(info + f'[info] Checking for {files} extensions.')
            for results in search(f'site:{domain} filetype:{files}', tld='com', lang='en', num=10, start=0, stop=None, pause=5):
                print(success + f'[{files} extension found] - {results}')
                url_path = results
                head, tail = os.path.split(url_path)
                urllib.request.urlretrieve(url_path, f'{domain}\\{tail}')
                request = request + 1
                if request == 100:
                    break
                time.sleep(1)
    except urllib.error.HTTPError:
        print(
            fail + f'\n[warn] Google is timing out queries. Wait a while and try again.\n')


if __name__ == "__main__":
    try:
        init()
        banner()
        domain = sys.argv[1]
        msdorker()
        file_exists = exists('.google-cookie')
        if file_exists is not None:
            os.remove('.google-cookie')
    except KeyboardInterrupt:
        print("\nYou either fat fingered this, or meant to do it. Either way, goodbye!\n")
        quit()
    except IndexError:
        print(fail + '\nSyntax - python3 msdorkdump.py <domain>\n')
