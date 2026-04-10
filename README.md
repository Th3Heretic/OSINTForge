# OSINTForge

OSINTForge is a modular Open-Source Intelligence (OSINT) framework designed to assist cybersecurity practitioners, investigators, and researchers in gathering and analysing publicly available data.

The tool provides both a Command-Line Interface (CLI) and a Graphical User Interface (GUI), enabling flexible usage depending on the user's workflow.

---

## Features

- Modular OSINT architecture
- GUI-based execution
- CLI support for scripting and automation
- Export functionality
- Multi-threaded scanning where applicable
- Built with Python for portability and extensibility

---

## Modules

| Module | Description |
|------|-------------|
| DNS Lookup | Retrieves A, MX, TXT records |
| WHOIS Lookup | Domain registration data |
| Port Scanner | Detects open TCP ports |
| Reverse DNS | Maps IP → hostname |
| SSL Certificate | Extracts certificate details |
| Directory Scanner | Finds hidden web directories |
| Subdomain Enumeration | Discovers subdomains via wordlist |
| Username Enumeration | Checks username across platforms |
| Traceroute | Maps network path |
| Metadata Extraction | Extracts file metadata using ExifTool |

---
## Installation

### CLI (Advanced)
Navigate to OSINTForge and type the following
```bash
pip install -r requirements.txt
```

>Automatic dependency installation is on the way, soon :)

---

## Usage

### GUI (Recommended)

>Double-click osintforge.exe inside the OSINTForge directory

or navigate to the OSINTForge directory and run:

```bash
python osintforge_gui.py
```

### CLI (Advanced)

#### Syntax
```bash
python osintforge.py -m <module> -t <target>
```
#### Example
```bash
python osintforge.py -m dns_lookup -t example.com
```

---

## Project Structure
```
OSINTForge/ 
├── modules/
├── data/
├── tools/
├── documentation/
├── osintforge.py
├── osintforge_gui.py
├── requirements.txt
├── README.md
├── LICENSE
├── references.txt
```

---

## External Dependencies

### ExifTool (Metadata module)
>The metadata extraction module requires ExifTool to function and is bundled in:
```
tools/windows/exiftool.exe
```
`(The module auto resolves the local filepath)`

---

## Ethical Use Disclaimer
```
This tool is intended strictly for:

Educational purposes
Authorised security testing
OSINT investigations

Unauthorised use against systems without permission may violate UK law, including the Computer Misuse Act 1990.
```

---

## Limitations


- Some platforms implement anti-bot protections (username enumeration may return partial results)
- DNS and WHOIS data may be limited by privacy protections
- External tools (e.g. ExifTool) must be correctly bundled


---

## Future Development


- GUI improvements (module descriptions, UX refinement)
- Unified JSON output format
- Module chaining (workflow automation)
- Report generation (PDF/Markdown)
- API integrations (Shodan, Censys)
