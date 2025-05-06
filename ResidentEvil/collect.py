#%%
import requests
from bs4 import BeautifulSoup

#%%

cookies = {
    '_gid': 'GA1.2.2105331318.1746563460',
    '_ga_DJLCSW50SC': 'GS2.1.s1746563460$o1$g1$t1746563502$j18$l0$h0',
    '_ga_D6NF5QC4QT': 'GS2.1.s1746563463$o1$g1$t1746563503$j20$l0$h0',
    '_ga': 'GA1.2.845417273.1746563460',
    'FCNEC': '%5B%5B%22AKsRol8rCQewG53BPaBS_17dSNVuG04L9xG8wkus43Q1DUHn_b9azN6VzXQOv0cLMQfv5pShJM4ZAGo80e3XbsghYovcJBrFk5LRsvOyoJnjV7lYYfKwrtBsom-RMKHoFOHpJ8q-BmFYZpdGf_ZwAH0P77De_J9t1A%3D%3D%22%5D%5D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.residentevildatabase.com/personagens/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

def get_content(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    return response

def get_basic_infos(soup):
    div_page = soup.find('div', class_ = 'td-page-content')
    paragrafo = div_page.find_all('p')[1]
    ems = paragrafo.find_all('em')
    data = {}
    for em in ems:
        chave, valor = em.text.split(':')
        chave = chave.strip(' ')
        data[chave] = valor.strip(' ')
    return data

def get_aparicoes(soup):
    lis = (soup.find('div', class_ = 'td-page-content')
               .find('h4')
               .find_next()
               .find_all('li'))

    aparicoes = [li.text for li in lis]
    return aparicoes

def get_personagem_infos(url):
    response = get_content(url)

    if response.status_code != 200:
        print('Não foi possível obter os dados.')
        return {}

    else:
        soup = BeautifulSoup(response.text)
        data = get_basic_infos(soup)
        data['Aparicoes'] = get_aparicoes(soup)
        return data
    
#%%
url = 'https://www.residentevildatabase.com/personagens/ada-wong/'
get_personagem_infos(url)

#%%

url = 'https://www.residentevildatabase.com/personagens/'
response = requests.get(url, headers=headers, cookies=cookies)
soup_personagens = BeautifulSoup(response.text)
soup_personagens


    