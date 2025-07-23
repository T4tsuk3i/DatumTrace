#!/bin/bash
domain="$1"
if [ -z "$domain" ]; then
  echo "Usage: $0 domain.com"
  exit 1
fi

echo "[+] WHOIS Info for $domain"
whois "$domain" | grep -Ei 'Registrant|Email|Name|Domain Status'
