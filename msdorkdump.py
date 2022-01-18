from ssl import SSL_ERROR_SSL
from urllib.error import HTTPError
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
global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']


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
    path = domain
    isdir = os.path.isdir(path)
    if isdir is True:
        pass
    else:
        os.mkdir(domain)
    os.chdir(domain)
    for files in file_types:
        try:
            file_exists = exists('.google-cookie')
            if file_exists == True:
                os.remove('.google-cookie')    
            print(info + f'[info] Checking for {files} extensions.')
            rand_user_agent = random.choice(user_agents)
            for results in search(f'site:{domain} filetype:{files}', tld='com', lang='en', num=100, start=0, stop=None, pause=5, user_agent=rand_user_agent):
                print(success + f'[{files} extension found] - {results}')
                url_path = results
                head, tail = os.path.split(url_path)
                urllib.request.urlretrieve(url_path, f'{tail}')
                request = request + 1
                if request == 100:
                    break            
                time.sleep(1)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(
                    fail + f'[Error Code 404] Web server is responding with 404 error. Skipping.')
                continue
            if e.code == 429:
                print(
                    fail + f'\n[Error Code 429] Google is timing out queries. Wait a while and try again.\n')
                quit()
            else:
                print(
                    fail + f'\n[warn] Error code {e.code} identified. Please create a new issue on the Github repo so it can be added.\n')
                continue
        except urllib.error.URLError:
            print(fail + f'[Error] File could not be downloaded. Skipping.')
            continue


if __name__ == "__main__":
    try:
        init()
        banner()
        domain = sys.argv[1]
        msdorker()
        print(info + f'\n[info] Dork scanning for {domain} completed.\n')

    except KeyboardInterrupt:
        print("\nYou either fat fingered this, or meant to do it. Either way, goodbye!\n")
        quit()
    except IndexError:
        print(fail + '\nSyntax - python3 msdorkdump.py <domain>\n')
