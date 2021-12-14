import requests
import colorama
import os
import concurrent.futures

colorama.init()
print('''
\033[32m
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                                    
''')

whatproxy = int(input('''
Which type of proxy do you need?
    
[1] Https 
[2] Socks4
[3] Socks5
    \n
[\]> '''))
if whatproxy == 1:
    out_file = "Https Proxies.txt"
    proxies = open(out_file,'wb')
    r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt' and'https://api.openproxylist.xyz/http.txt')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
    proxylist = []
    url = 'http://icanhazip.com/'

    checker = input("Do you want to check the proxies (y/n)?: ").lower()
    if checker == 'y':
        os.system('cls')
        with open('Https Proxies.txt','r') as f:
            for line in f:
                line = line.replace('\n','')
                tmp = line.split(':')
                proxies = {
                    'http':'http://'+tmp[0]+'/',
                    'https':'http://'+tmp[0]+'/'
                }
                proxylist.append(proxies)
                def extract(proxy):
                    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36'}
                    for proxy in proxylist:
                        try:
                            r = requests.get(url, headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
                            print(r.json(), '\033[32m ~ Works')
                            data = open("Working Proxies.txt",'wb')
                            data.write(r.json())
                        except:
                            pass
                        return proxy
                    proxies.close()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(extract, proxylist)

        exit()  

elif whatproxy == 2:
    r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt'and 'https://api.openproxylist.xyz/socks4.txt')
    out_file = "Socks4 Proxies.txt"
    proxies = open(out_file,'wb')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
    proxylist = []
    checker = input("Do you want to check the proxies (y/n)?: ").lower()
    if checker == 'y':
        os.system('cls')
        with open('Socks4 Proxies.txt','r') as f:
            for line in f:
                line = line.replace('\n','')
                tmp = line.split(':')
                proxies = {
                    'http':'http://'+tmp[0]+'/',
                    'https':'http://'+tmp[0]+'/'
                }
                proxylist.append(proxies)
                def extract1(proxy):
                    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36'}
                    for proxy in proxylist:
                        try:
                            r = requests.get(url, headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
                            print(r.json(), '\033[32m ~ Works')
                            data = open("Working Proxies.txt",'wb')
                            data.write(r.json())
                        except:
                            pass
                        return proxy
                    proxies.close()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(extract1, proxylist)

        exit()

elif whatproxy == 3:
    r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt' and 'https://api.openproxylist.xyz/socks5.txt')
    out_file = "Socks5 Proxies.txt"
    proxies = open(out_file,'wb')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
    proxylist = []
    checker = input("Do you want to check the proxies (y/n)?: ").lower()
    if checker == 'y':
        os.system('cls')
        with open('Socks4 Proxies.txt','r') as f:
            for line in f:
                line = line.replace('\n','')
                tmp = line.split(':')
                proxies = {
                    'http':'http://'+tmp[0]+'/',
                    'https':'http://'+tmp[0]+'/'
                }
                proxylist.append(proxies)
                def extract2(proxy):
                    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36'}
                    for proxy in proxylist:
                        try:
                            r = requests.get(url, headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
                            print(r.json(), '\033[32m ~ Works')
                            data = open("Working Proxies.txt",'wb')
                            data.write(r.json())
                        except:
                            pass
                        return proxy
                    proxies.close()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(extract2, proxylist)

    proxies.close()

else:
    print("Not a valid choice!")
