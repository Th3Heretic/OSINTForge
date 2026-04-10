# DNS Lookup

## Description

The DNS Lookup module retrieves key DNS records for a given domain, providing insight into its infrastructure, email configuration, and verification mechanisms.

The module queries commonly used record types and presents them in a structured, readable format.

---

## How It Works

The module:

1. Accepts a domain name as input.
2. Uses the `dnspython` library to query DNS records.
3. Retrieves and displays the following record types:
   - A (IPv4 address mapping)
   - MX (mail exchange servers)
   - TXT (text-based records such as SPF, DKIM, verification)
4. Handles common DNS errors such as:
   - Non-existent domains
   - Missing record types
   - Unreachable nameservers

---

## Usage

### GUI

1. Open OSINTForge.
2. Select **DNS Lookup**.
3. Enter a domain name (e.g. `example.com`).
4. Click **Run DNS Lookup**.

---

### CLI

```bash
python osintforge.py -m dns_lookup -t example.com
```

#### Example Output
```bash
Running DNS Lookup for: example.com

A Records:
 - 93.184.216.34

MX Records:
 - 10 mail.example.com.
 - 20 mail2.example.com.

TXT Records:
 - "v=spf1 include:_spf.example.com ~all"
```

#### Output Explanation

<u>A Records</u>
- Maps a domain to its IPv4 address.
- Useful for identifying hosting infrastructure.

<u>MX Records</u>
- Defines mail servers responsible for handling email.
- Lower priority values indicate primary servers.

<u>TXT Records</u>
- Stores arbitrary text data.
- Common uses include:
  - SPF (email validation)
  - DKIM (email signing)
  - Domain verification (e.g. Google, Microsoft)

---

## Common Use Cases
- Identifying a domain’s hosting infrastructure
- Analysing email configuration and security (SPF, DKIM, DMARC)
- Supporting reconnaissance during OSINT investigations
- Verifying domain ownership and service integrations

---

## Limitations
- Only a limited set of record types are queried (A, MX, TXT)
- Does not currently support IPv6 (AAAA) or CNAME lookups
- Results depend on DNS availability and external resolver behaviour
- Some domains may restrict or obscure DNS data

---

## Future Improvements
- Support additional record types (AAAA, NS, CNAME, SOA)
- Batch processing of multiple domains
- CSV/JSON export functionality
- DNS misconfiguration detection (e.g. missing SPF/DMARC)
- Zone transfer (AXFR) testing

---

## Ethical Considerations

#### DNS lookups are generally passive and non-intrusive, but should still be used responsibly.

#### This module should only be used as part of authorised investigations or educational activities.