import argparse
from modules.email_harvest import scrape_emails
from modules.username_lookup import scrape_usernames

parser = argparse.ArgumentParser(description="🕵️ OSINT Data Scraper CLI")
parser.add_argument("target", help="Target domain or username")
parser.add_argument("--emails", action="store_true", help="Scrape emails")
parser.add_argument("--users", action="store_true", help="Scrape usernames and profiles")
args = parser.parse_args()

if args.emails:
    print("\n[+] Scraping Emails...")
    emails = scrape_emails(args.target)
    for email in emails:
        print("  -", email)

if args.users:
    print("\n[+] Scraping Social Usernames...")
    users = scrape_usernames(args.target)
    for user in users:
        print("  -", user)
