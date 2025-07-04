# FIIs Scraper - MXRF11

Este projeto é um script simples em Python que utiliza `requests` e `BeautifulSoup` para coletar dados públicos da página do fundo imobiliário [MXRF11](https://fiis.com.br/mxrf11/) no site https://fiis.com.br/.

## 🚀 Funcionalidade

O script realiza:

- Acesso ao site do FII.
- Coleta do nome do fundo (título `<h1>`).
- Coleta do primeiro valor encontrado com a classe `.value` (ex: valor da cota, dividend yield etc.).

## 🧪 Pré-requisitos

- Python 3.7 ou superior
- `requests`
- `beautifulsoup4`

Você pode instalar as dependências com:

```bash
pip install -r requirements.txt
```

## 📦 Estrutura do código

```python
import requests
from bs4 import BeautifulSoup

url = "https://fiis.com.br/mxrf11/"
headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

name = soup.find_all('h1')
value = soup.find_all('span', class_='value')

print("Name:", name[0].text)
print("Value:", value[0].text)
```

## 📄 Exemplo de saída

```bash
Fetching data from https://fiis.com.br/mxrf11/
Status: 200
Name: MXRF11 - Maxi Renda FII
Value: R$ 10,50
```

## 📌 Observações

- O site pode alterar a estrutura HTML a qualquer momento, então o script pode precisar de ajustes futuros.
- O uso de scraping deve respeitar os termos de uso do site original.

## 📃 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
