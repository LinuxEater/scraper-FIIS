import requests
from bs4 import BeautifulSoup



url = "https://fiis.com.br/mxrf11/"
print(f"Fetching data from {url}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

name = soup.find_all('h1')
value = soup.find_all('span', class_='value')


print("Name:", name[0].text)
print("Value:", value[0].text)
