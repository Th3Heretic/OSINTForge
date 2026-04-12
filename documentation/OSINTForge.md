# OSINTForge - Open-Source Intelligence Framework

## Overview

OSINTForge is a modular, Python-based open-source intelligence (OSINT) framework designed to assist cybersecurity practitioners, investigators, and researchers in gathering and analysing publicly available information.

The tool provides both a graphical user interface (GUI) and command-line interface (CLI), allowing users to execute targeted intelligence-gathering modules in a structured and efficient manner.

Each module focuses on a specific aspect of OSINT, enabling flexible workflows and extensibility.

---

## Key Features

- Modular architecture for scalability and maintainability  
- GUI-based interaction using Tkinter  
- CLI support for automation and scripting  
- Threaded execution in selected modules for improved performance  
- Local and network-based intelligence gathering capabilities  
- Designed for ethical and controlled environments  

---

## Current Modules

### Network & Infrastructure

- DNS Lookup  
  Retrieves A, MX, and TXT records for a domain  

- Reverse DNS  
  Maps IP addresses to associated hostnames  

- SSL Certificate  
  Extracts certificate metadata from remote hosts  

- Traceroute  
  Maps network paths to a target host  

- Port Scanner  
  Performs TCP connect scans on common ports  

---

### Web & Enumeration

- Directory Scanner  
  Identifies accessible directories on a target web server  

- Subdomain Enumeration  
  Performs wordlist-based discovery of subdomains  

---

### Identity & OSINT Correlation

- Username Enumeration  
  Checks for username presence across multiple platforms  

---

### File Analysis

- Metadata Extraction  
  Extracts embedded metadata from files using a bundled ExifTool binary  

---

### Domain Intelligence

- WHOIS Lookup  
  Retrieves domain registration and ownership data  

---

## Deprecated Modules

The following modules have been deprecated due to reliability or dependency issues:

- Email Validation  
  Limited to syntax and MX checks; unable to verify mailbox existence reliably  

- IP Geolocation  
  Dependent on an external API which is no longer operational  

- Website Metadata  
  Inconsistent results and limited investigative value  

These modules have been removed from the GUI to maintain tool reliability.

---

## Design Principles

OSINTForge is built around the following principles:

- Modularity  
  Each feature is implemented as an independent module  

- Simplicity  
  Clear inputs and readable outputs  

- Reliability  
  Preference for local processing over external dependencies  

- Ethical Use  
  All modules are designed for authorised and controlled environments only  

---

## Future Development Roadmap

Planned enhancements include:

### Core Improvements

- Unified output format (JSON / CSV export across all modules)  
- Improved error handling and logging  
- Module chaining (e.g. WHOIS → DNS → Subdomain Enumeration)  
- Performance optimisation using threading and async operations  

### New Modules

- Reverse Image Search  
- Social Media Scraper  
- File Hash Calculator  
- Code Repository Search  
- Malware URL Scanner  
- Paste/Leak Search  
- OSINT Report Generator  
- Graph-Based Relationship Mapping  

### Interface Enhancements

- Improved GUI layout and usability  
- Module descriptions and contextual help  
- Optional web-based dashboard  

---

## Ethical Considerations

OSINTForge is intended strictly for ethical use.

Users must ensure that all activities conducted with this tool:

- Are authorised  
- Comply with applicable laws and regulations  
- Respect privacy and data protection principles  

Misuse of this tool may result in legal or disciplinary consequences.

---

## Summary

OSINTForge provides a structured and extensible approach to open-source intelligence gathering, combining multiple investigative techniques into a single platform.

Its modular design, combined with both GUI and CLI interfaces, makes it suitable for both educational use and practical cybersecurity workflows.