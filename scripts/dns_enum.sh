#!/bin/bash
domain="$1"
echo "[+] DNS Records for $domain"
dig any "$domain" +noall +answer

echo -e "\n[+] Subdomains from common wordlist:"
for sub in www mail ftp blog test dev admin; do
  dig "$sub.$domain" +short | grep -v '^$' && echo "  → $sub.$domain"
done
