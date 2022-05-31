import argparse
import sys
import requests
from threading import Thread
import multiprocessing
import asyncio
import random
from bs4 import BeautifulSoup
import builtwith



parser = argparse.ArgumentParser(description="Python Bruteforce Login")
parser.add_argument('--url', help="Website to target", required=True)
parser.add_argument('--extension', help="Extensions to find files (Ex: exe) Default .php", required=False)
parser.add_argument('--wordlist', help="Wordlist of passwords to use", required=True)
args = parser.parse_args()


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

proxy = {
  'http': 'http://127.0.0.1:8080',
}

user_agent_list = [
'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2'
'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16'
'Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16'
'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14'
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14'
'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02'
'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00'
'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00'
'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00'
'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.1 (KHTML, like Gecko) Safari/125'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-ch) AppleWebKit/312.1.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-ca) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko)'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.1.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312.3.1'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'
'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'
'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
]

def directories(WORDLIST_FILENAME):
       global line
       print("---------------------------------------------------------------------------------------------------------------------------------------")
       print(f"{bcolors.WARNING}[+] BruteForcing Files...{bcolors.RESET}",f"{bcolors.RESET}")
       wordlist = list()
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                my_str=line.strip()
                user_agent = random.choice(user_agent_list)
                headers = {"User-Agent": user_agent}
                uuuuu = final_url+"/"+my_str
                uuuuu2 = final_url+"/"+my_str+"."+extensionn
                lista = list()
                ttt = requests.get(uuuuu,proxies=False,headers=headers)
                ttt2 = requests.get(uuuuu2,proxies=False,headers=headers)
                if ttt.status_code == 200:
                    delete = requests.delete(uuuuu)
                    get = requests.get(uuuuu)
                    post = requests.post(uuuuu)
                    head = requests.head(uuuuu)
                    put = requests.put(uuuuu,proxies=False)
                    patch = requests.patch(uuuuu)
                    if get.status_code == 200:
                        lista.append("GET")
                        if post.status_code == 200:
                            lista.append("POST")
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista) 
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)


                        else:
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                
                        

                                    

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)

                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)


                            
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                    
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                           

                    else:
                        if post.status_code == 200:
                            lista.append("POST")
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)

                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                        else:
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
     
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista) 
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
        

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)


                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                

                elif ttt.status_code == 404:
                    pass
                else:
                    pass
                if ttt2.status_code == 200:
                    print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu2)
                elif ttt2.status_code == 404:
                    pass
                else:
                    pass
                

def files():
    title1 = soup.title
    title2 = str(title1)
    caca = builtwith.parse(args.url)

    print(f"{bcolors.OK}[+] Title Of Page: {bcolors.RESET}",title2[7:-8])

    print(f"{bcolors.OK}[+] Technologies: {bcolors.RESET}",caca)


    c = soup.find_all('a')
    print("------------------------------------------------------------------------------------------------------------------")
    print(f"{bcolors.OK}[+] PHP Files: {bcolors.RESET}")

    for a in soup.findAll('a'):
        try:
            if a['href'].endswith('.php'):
                if (a['href'][:5]) == "https":
                    pass
                else:    
                    if (a['href'][:4]) == "http":
                        pass
                    else:    
                        print(a['href'])
        except KeyError:
            pass

    for link in soup.find_all('link'):
        try:
            if link['href'].endswith('.php'):
                if (link['href'][:5]) == "https":
                    pass
                else:    
                    if (link['href'][:4]) == "http":
                        pass
                    else:    
                        print(link['href'])
        except KeyError:
            pass
                    
    for h3 in soup.findAll('h3'):
        try:
            if h3['href'].endswith('.php'):
                if (h3['href'][:5]) == "https":
                    pass
                else:    
                    if (h3['href'][:4]) == "http":
                        pass
                    else:    
                        print(h3['href'])
        except KeyError:
            pass

    for h2 in soup.findAll('h2'):
        try:
            if h2['href'].endswith('.php'):
                if (h2['href'][:5]) == "https":
                    pass
                else:    
                    if (h2['href'][:4]) == "http":
                        pass
                    else:    
                        print(h2['href'])
        except KeyError:
            pass

    for h1 in soup.findAll('h1'):
        try:
            if h1['href'].endswith('.php'):
                if (h1['href'][:5]) == "https":
                    pass
                else:    
                    if (h1['href'][:4]) == "http":
                        pass
                    else:    
                        print(h1['href'])
        except KeyError:
            pass

    for h4 in soup.findAll('h4'):
        try:
            if h4['href'].endswith('.php'):
                if (h4['href'][:5]) == "https":
                    pass
                else:    
                    if (h4['href'][:4]) == "http":
                        pass
                    else:    
                        print(h4['href'])
        except KeyError:
            pass

    for h5 in soup.findAll('h5'):
        try:
            if h5['href'].endswith('.php'):
                if (h5['href'][:5]) == "https":
                    pass
                else:    
                    if (h5['href'][:4]) == "http":
                        pass
                    else:    
                        print(h5['href'])
        except KeyError:
            pass

    print(f"{bcolors.OK}[+] JavaScript Files: {bcolors.RESET}")

    for a in soup.findAll('a'):
        try:
            if a['href'].endswith('.js'):
                if (a['href'][:5]) == "https":
                    pass
                else:    
                    if (a['href'][:4]) == "http":
                        pass
                    else:    
                        print(a['href'])
        except KeyError:
            pass

    for script in soup.find_all('script'):
        try:
            if script['src'].endswith('.js'):
                if (script['src'][:5]) == "https":
                    pass
                else:    
                    if (script['src'][:4]) == "http":
                        pass
                    else:    
                        print(script['src'])
        except KeyError:
            pass

    print(f"{bcolors.OK}[+] JSON Files: {bcolors.RESET}")

    for a in soup.findAll('a'):
        try:
            if a['href'].endswith('.json'):
                if (a['href'][:5]) == "https":
                    pass
                else:    
                    if (a['href'][:4]) == "http":
                        pass
                    else:    
                        print(a['href'])
        except KeyError:
            pass

    for link in soup.find_all('link'):
        try:
            if link['href'].endswith('.json'):
                if (link['href'][:5]) == "https":
                    pass
                else:    
                    if (link['href'][:4]) == "http":
                        pass
                    else:    
                        print(link['href'])
        except KeyError:
            pass
                    
    for h3 in soup.findAll('h3'):
        try:
            if h3['href'].endswith('.json'):
                if (h3['href'][:5]) == "https":
                    pass
                else:    
                    if (h3['href'][:4]) == "http":
                        pass
                    else:    
                        print(h3['href'])
        except KeyError:
            pass

    for h2 in soup.findAll('h2'):
        try:
            if h2['href'].endswith('.json'):
                if (h2['href'][:5]) == "https":
                    pass
                else:    
                    if (h2['href'][:4]) == "http":
                        pass
                    else:    
                        print(h2['href'])
        except KeyError:
            pass

    for h1 in soup.findAll('h1'):
        try:
            if h1['href'].endswith('.json'):
                if (h1['href'][:5]) == "https":
                    pass
                else:    
                    if (h1['href'][:4]) == "http":
                        pass
                    else:    
                        print(h1['href'])
        except KeyError:
            pass

    for h4 in soup.findAll('h4'):
        try:
            if h4['href'].endswith('.json'):
                if (h4['href'][:5]) == "https":
                    pass
                else:    
                    if (h4['href'][:4]) == "http":
                        pass
                    else:    
                        print(h4['href'])
        except KeyError:
            pass

    for h5 in soup.findAll('h5'):
        try:
            if h5['href'].endswith('.json'):
                if (h5['href'][:5]) == "https":
                    pass
                else:    
                    if (h5['href'][:4]) == "http":
                        pass
                    else:    
                        print(h5['href'])
        except KeyError:
            pass
    print(f"{bcolors.OK}[+] XML Files: {bcolors.RESET}")

    for a in soup.findAll('a'):
        try:
            if a['href'].endswith('.xml'):
                if (a['href'][:5]) == "https":
                    pass
                else:    
                    if (a['href'][:4]) == "http":
                        pass
                    else:    
                        print(a['href'])
        except KeyError:
            pass

    for link in soup.find_all('link'):
        try:
            if link['href'].endswith('.xml'):
                if (link['href'][:5]) == "https":
                    pass
                else:    
                    if (link['href'][:4]) == "http":
                        pass
                    else:    
                        print(link['href'])
        except KeyError:
            pass
                    
    for h3 in soup.findAll('h3'):
        try:
            if h3['href'].endswith('.xml'):
                if (h3['href'][:5]) == "https":
                    pass
                else:    
                    if (h3['href'][:4]) == "http":
                        pass
                    else:    
                        print(h3['href'])
        except KeyError:
            pass

    for h2 in soup.findAll('h2'):
        try:
            if h2['href'].endswith('.xml'):
                if (h2['href'][:5]) == "https":
                    pass
                else:    
                    if (h2['href'][:4]) == "http":
                        pass
                    else:    
                        print(h2['href'])
        except KeyError:
            pass

    for h1 in soup.findAll('h1'):
        try:
            if h1['href'].endswith('.xml'):
                if (h1['href'][:5]) == "https":
                    pass
                else:    
                    if (h1['href'][:4]) == "http":
                        pass
                    else:    
                        print(h1['href'])
        except KeyError:
            pass

    for h4 in soup.findAll('h4'):
        try:
            if h4['href'].endswith('.xml'):
                if (h4['href'][:5]) == "https":
                    pass
                else:    
                    if (h4['href'][:4]) == "http":
                        pass
                    else:    
                        print(h4['href'])
        except KeyError:
            pass

    for h5 in soup.findAll('h5'):
        try:
            if h5['href'].endswith('.xml'):
                if (h5['href'][:5]) == "https":
                    pass
                else:    
                    if (h5['href'][:4]) == "http":
                        pass
                    else:    
                        print(h5['href'])
        except KeyError:
            pass

    print(f"{bcolors.OK}[+] Others Files Or Directories: {bcolors.RESET}")

    for a in soup.findAll('a'):
        try:
            if a['href'].endswith('/'):
                if (a['href'][:5]) == "https":
                    pass
                else:    
                    if (a['href'][:4]) == "http":
                        pass
                    else:    
                        print(a['href'])
        except KeyError:
            pass



def file_upload():
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{bcolors.OK}[+] Searching File Uploads...: {bcolors.RESET}")

    if '<input type="file"' in aaa:
        tita = len(soup.find_all('input',type="file"))
        if tita == 1:
            print(f"{bcolors.OK}[+] Posible File Upload Detected ={bcolors.RESET}",soup.find_all('input',type="file"))
        elif tita == 0:
            print(f"{bcolors.FAIL}0 File Uploads Detected{bcolors.RESET}")

    else:
        print(f"{bcolors.FAIL}0 File Uploads Detected{bcolors.RESET}")


global test

try:
    test = requests.get(args.url)
    print(f"{bcolors.WARNING}[+] CONNECTING WITH TARGET{bcolors.RESET}")
except ConnectionRefusedError():
    print(f"{bcolors.FAIL}[+] CONNECTION REFUSED{bcolors.RESET}")

titaa = requests.get(args.url)

aaa = str(titaa.content)
global soup
soup = BeautifulSoup(titaa.content, 'html.parser')

if titaa.status_code == 404:
    print(f"{bcolors.FAIL}Failed connecting to Target{bcolors.RESET}")
else:
    files()
    file_upload()

if args.url[-1] == "/":
    final_url = args.url[:-1]
else:
    final_url = args.url 

if args.extension == None:
	extensionn = "php"
else:
	extensionn = args.extension

directories(args.wordlist)