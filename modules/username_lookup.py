import requests
from modules.utils import load_config

def scrape_usernames(username):
    config = load_config()
    found = []

    for platform in config['username_sources']:
        if not platform['enabled']:
            continue
        url = platform['url'].format(username=username)
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                found.append(f"{platform['platform']}: {url}")
        except Exception:
            continue
    return found
