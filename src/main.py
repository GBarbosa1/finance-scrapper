import requests
from handlers.logger import logging
logger = logging.getLogger()

url = 'https://fiis.com.br/alzr11/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    html_content = response.text
    if 'P/VP' in html_content:
        a = html_content.find('P/VP')
        print(html_content[a-16:a-12])
        
except Exception as e:
    logging.fatal(f"Failed to retrieve the fii data, error: {e}")

