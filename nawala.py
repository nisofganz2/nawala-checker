import requests
import re, time, os, sys
import json, socket
from multiprocessing import Pool
from rich import print as cetak
from pystyle import Colors,Colorate,Write
from rich.panel import Panel as nel
from colorama import Fore,Style,init
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua1 = {'User-Agent': UserAgent().random}
import requests,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)
red = Fore.RED
cyan = Fore.CYAN
green = Fore.GREEN 
yellow = Fore.YELLOW
white = Fore.WHITE
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clear_console():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')
        
def display_intro():
    Write.Print("─══════════════════════════ቐቐ══════════════════════════─\n", Colors.blue_to_purple, interval=0.01)
    text = f""" 
 /$$   /$$ /$$                      /$$$$$$ 
| $$$ | $$|__/                     /$$__  $$
| $$$$| $$ /$$  /$$$$$$$  /$$$$$$ | $$  \__/
| $$ $$ $$| $$ /$$_____/ /$$__  $$| $$$$    
| $$  $$$$| $$|  $$$$$$ | $$  \ $$| $$_/    
| $$\  $$$| $$ \____  $$| $$  | $$| $$      
| $$ \  $$| $$ /$$$$$$$/|  $$$$$$/| $$      
|__/  \__/|__/|_______/  \______/ |__/     

# CREATED BY : t.me/nisofganz2"""

    for N, line in enumerate(text.split("\n")):
        print(Colorate.Horizontal(Colors.red_to_green, line, 1))
        time.sleep(0.05)
    Write.Print("\n─══════════════════════════ቐቐ══════════════════════════─\n\n", Colors.blue_to_purple, interval=0.01)
def check_domains():
    try: 
        id_telegram = int(input(f"\t{red}[{white}#{red}]{white} Input ID Telegram (0 for none): ") or 0)
        domain_list = [line.strip() for line in open(input(f"\t{red}[{white}#{red}]{white} LIST SITE : ")) if line.strip()]
        result_directory = os.path.join('results', 'CheckNawala')
        os.makedirs(result_directory, exist_ok=True)

        for domain in domain_list:
            try:
                ip_address = socket.gethostbyname(domain)
                domain = f'http://{re.sub(r"https?://", "", domain)}'
                csrf = re.findall(r'name="csrf_token" value="(.*?)"', requests.get('https://trustpositif.kominfo.go.id/', headers={'User-Agent': UserAgent().random}, verify=False).content.decode("utf-8"))[0]
                response = requests.post('https://trustpositif.kominfo.go.id/Rest_server/getrecordsname_home', data={'csrf_token': csrf, 'name': domain}, headers={'User-Agent': UserAgent().random}, verify=False, timeout=15).content.decode("utf-8")
                status = json.loads(response)['values'][0]['Status']
                
                if status == 'Ada':
                    logging.info(f'{yellow}|- {white}{domain} {yellow}| {red}[ FOUND NAWALA! ]')
                    with open(os.path.join(result_directory, 'found_nawala.txt'), "a+") as file:
                        file.write(f'https://{domain}\n')
                    if id_telegram:
                        requests.get(f'https://api.telegram.org/bot(your token)/sendMessage?chat_id={id_telegram}&text=Domain: {domain}\nIP: {ip_address}\nFound Nawala!', timeout=20)
                else:
                    logging.info(f'{yellow}|- {white}{domain} {yellow}| {green}[ AMAN! ]')
            except Exception as e:
                logging.error(f"Error processing {domain}: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        display_intro()
        check_domains()
    except Exception as e:
        logging.error(f"An error occurred in main: {e}")