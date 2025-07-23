import re
import requests
from bs4 import BeautifulSoup
from modules.utils import load_config, build_headers

def scrape_emails(target):
    config = load_config()
    headers = build_headers(config)
    emails = set()

    for src in config['email_sources']:
        if not src['enabled']:
            continue
        query = src['query'].format(target=target)
        search_url = config['search_engines']['google']['base_url'].format(query=query)
        try:
            res = requests.get(search_url, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, 'html.parser')
            found = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", soup.text)
            emails.update(found)
        except Exception as e:
            print(f"[!] Failed: {query} → {e}")
    return list(emails)
