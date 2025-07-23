import re

def extract_user_profiles(text):
    patterns = [
        r"https?://(www\.)?github\.com/[a-zA-Z0-9_-]+",
        r"https?://(www\.)?twitter\.com/[a-zA-Z0-9_]+",
        r"https?://(www\.)?instagram\.com/[a-zA-Z0-9_.]+"
    ]
    found = []
    for pattern in patterns:
        found += re.findall(pattern, text)
    return found
