import re

def detect_emails_from_text(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

if __name__ == "__main__":
    with open("../../test_data/example_html.html") as f:
        data = f.read()
    print(detect_emails_from_text(data))
