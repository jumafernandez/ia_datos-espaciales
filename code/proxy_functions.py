import requests
import random
from bs4 import BeautifulSoup

def fetch_proxies_freeproxy(n):
    url = "https://free-proxy-list.net/"
    response = requests.get(url)
    cantidad = 0
    if response.status_code == 200:
        print(f'\nfree-proxy-list respondió exitosamente. Se buscará almacenar {n} proxies.')
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')
        proxies = []
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 2:
                    ip = columns[0].text
                    port = columns[1].text
                    google = columns[5].text
                    https = columns[6].text
                    if google=='yes' and https=='yes':
                        proxy = f"{ip}:{port}"
                        print(f'Se incorpora el proxy: {proxy}.')
                        proxies.append(proxy)
                        cantidad = cantidad + 1
                        if cantidad == n:
                            return proxies
            print(f'Se encontraron {len(proxies)} proxies https.')
            return proxies
    else:
        print("Error al obtener la lista de proxies.")
        return []

def fetch_proxies_sslproxies(n):
    url = "https://www.sslproxies.org/"
    response = requests.get(url)
    cantidad = 0
    if response.status_code == 200:
        print(f'\nsslproxies respondió exitosamente. Se buscará almacenar {n} proxies.')
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')
        proxies = []
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 2:
                    ip = columns[0].text
                    port = columns[1].text
                    google = columns[5].text
                    https = columns[6].text
                    if google=='yes' and https=='yes':
                        proxy = f"{ip}:{port}"
                        print(f'Se incorpora el proxy: {proxy}.')
                        proxies.append(proxy)
                        cantidad = cantidad + 1
                        if cantidad == n:
                            print(f'Se encontraron {len(proxies)} proxies https.')
                            return proxies
            print(f'Se encontraron {len(proxies)} https validados contra Google.')
            return proxies
    else:
        print("Error al obtener la lista de proxies.")
        return []


def test_proxy(proxy):
    try:
        http_proxy = {"http": proxy}
        https_proxy = {"https": proxy}
        http_response = requests.get("http://www.google.com", proxies=http_proxy, timeout=5)
        https_response = requests.get("https://www.google.com", proxies=https_proxy, timeout=5)
        return http_response.status_code == 200 and https_response.status_code == 200
    except requests.exceptions.RequestException:
        return False
    
def get_valid_proxies(all_proxies):
    valid_proxies = []
    num_proxies = len(all_proxies)
    print(f'\nVerificación de proxies válidos contra Google, se necesitan {num_proxies}:')
    random.shuffle(all_proxies)
    for proxy in all_proxies:
        if test_proxy(proxy):
            print(f'Proxy válido: {proxy}.')
            valid_proxies.append({"http": f"http://{proxy}", "https": f"https://{proxy}"})
            if len(valid_proxies) == num_proxies:
                break
        else:
            print(f'Time out proxy: {proxy} (NO VÁLIDO).')
            
    return valid_proxies

def get_random_proxy(proxies):
    proxy = random.choice(proxies)
    return proxy

# Ejemplo de uso
# proxies_list_1 = fetch_proxies_sslproxies(30)
# proxies_list_2 = fetch_proxies_freeproxy(30)

# validos_1 = get_valid_proxies(proxies_list_1)
# validos_2 = get_valid_proxies(proxies_list_2)
# proxys_validos = validos_1
# proxys_validos.extend(validos_2)

# print(proxys_validos)