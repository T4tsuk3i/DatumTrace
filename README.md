```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/T4tsuk3i/DatumTrace/master/datum.png" width="300" alt="DatumTrace Banner"/>
</p>

<h1 align="center">🕵️‍♂️ DatumTrace</h1>

<p align="center">
  <i>A modular OSINT scraping framework for gathering emails, usernames, and social data from names or domains</i>
</p>

---

## 🧠 About

**DatumTrace** is a modular, CLI-based OSINT data scraper that pulls:

- 📧 Emails  
- 🧑‍💻 Usernames  
- 🌐 Social profiles  

based on **name or domain keywords**, across multiple public sources.

> 💡 It is not released as a unified tool. Instead, each module is published separately as an "experiment" for flexibility and ethical control.

---

## 🛠️ Tech Stack

- Python 3.11+
- `requests`, `aiohttp`, `asyncio`
- `BeautifulSoup`
- YAML for source config
- Works 100% on **Linux Terminal**
- Modular file layout for easy experimentation

---

## 🚀 Usage

> ⚠️ Ensure dependencies are installed:

```bash
pip install -r requirements.txt
````

> 🔍 Run the OSINT scraper with a name or domain:

```bash
python main.py --target "elonmusk"
```

> 📂 Output will be saved to:

```bash
data/output.json
```

---

## 📑 Example Output

```json
{
  "emails": ["contact@domain.com", "admin@xyz.org"],
  "usernames": ["elonmusk", "realelon"],
  "social_profiles": [
    "https://twitter.com/elonmusk",
    "https://github.com/elonmusk"
  ]
}
```

---

## ⚙️ Add New Sources

New scrapers can be added in `sources/sources.yaml`. Each source includes:

```yaml
- name: "Twitter"
  type: "profile"
  url: "https://twitter.com/{query}"
  enabled: true
```

---

## 📜 Disclaimer

> This project is intended for **educational and ethical research** purposes only.
> Do not use this tool to target, harass, or collect data on individuals without their explicit consent.
> The authors take **no responsibility** for misuse.

---

## 🧪 Experiments Only

This is a **research framework**, not a weaponized tool.

* Modules are decoupled and meant to be studied, modified, or extended.
* Each one can be tested independently.
* CLI only — no GUI, no auto-spam behavior.

---

<p align="center"><b>Built for security education, not exploitation.</b></p>
```
