<h1><b><u>OSINTForge Investigation Tool</u></b></h1>

Please note, some of these modules aren't perfect and may not work for whatever reason on your system. Also, this is a 
passion project so more updates or modules may be released at a later time but don't expect them to be regular. 

Thanks, and I hope you enjoy using this early access OSINT tool :)

A brief rundown of the project structure:
OSINTForge/
├── documentation            # Filled with usage documentation for each module 
│   ├── directory_scanner.txt
│   ├── dns_lookup.txt
│   ├── metadata_extraction.txt
│   ├── port_scanner.txt
│   ├── reverse_dns.txt
│   ├── ssl_certificate.txt
│   ├── reverse_image_search.txt
│   ├── OSINTForge.txt
│   ├── subdomain_enum.txt
│   ├── ip_geolocation.txt
│   ├── website_metadata.txt
│   └── whois_lookup.txt
├── modules/
│   ├── __init__.py          # To mark this as a package
│   ├── directory_scanner.py # Ninth module
│   ├── dns_lookup.py        # First module
│   ├── email_validation.py  # Eighth module
│   ├── metadata_extraction.py # Second module
│   ├── port_scanner.py      # Sixth module
│   ├── reverse_dns.py       # Eleventh module
│   ├── ssl_certificate.py   # Tenth module
│   ├── subdomain_enum.py    # Fifth module
│   ├── traceroute.py        # Twelfth module
│   ├── ip_geolocation.py    # Third module
│   ├── website_metadata.py  # Seventh module
│   └── whois_lookup.py      # Fourth module
├── references.txt           # Sources and methodology documentation
├── osintforge.py            # Main CLI script
├── README.md                # Project overview
├── LICENSE                  # GPL v3 license
└── requirements.txt         # Python dependencies

Installing the dependencies:
- using the terminal navigate to the project folder
- to check that the requirements.txt is present, run: 
>ls 
- Once you have confirmed its presence in the cwd run:
>pip install -r requirements.txt


To use the dns_lookup tool:
_python osintforge.py -m dns_lookup -t example.com_

    -m is specifying the module to use
    -t specifies the target domain

note: The target should be a domain name, not a full URL.


To use the metadata_extraction tool:
_python osintforge.py -m metadata_extraction -t /absolute/path/to/image.jpg_

    -m once again specifies the module
    -t is specifying the target image filepath


To use the ip_geolocation tool:
_python osintforge.py -m ip_geolocation -t 0.0.0.0_

    -t is used to specify a target IP address
    - can be used in conjuntion with the dns_lookup and subdomain_enum modules


To use the whois_lookup tool:
_python osintforge.py -m whois_lookup -t example.com_

    -t specifies a target domain name


To use the subdomain_enum tool:
_python osintforge.py -m subdomain_enum -t example.com_

    -t specifies a target domain name

To use the port_scanner tool:
_python osintforge.py -m port_scanner -t 8.8.8.8_

    -t specifies a target IP to audit for open ports

To use the website_metadata tool:
_python osintforge.py -m website_metadata -t example.com_

    -t specifies a domain name

To use the email_validation tool:
_python osintforge.py -m email_validation -t email@example.com_

    -t specifies an email address

To use the directory_scanner tool:
_python osintforge.py -m directory_scanner -t https://example.com_

    -t specifies a URL to inspect

To use the ssl_certificate tool:
_python osintforge.py -m ssl_certificate -t example.com_

    -t specifies the target URL or IP

To use the reverse_dns tool:
_python osintforge.py -m reverse_dns -t 8.8.8.8_

    -t specifies the IP assigned to a domain

To use the traceroute tool:
_python osintforge.py -m traceroute -t example.com_

    -t specifies a target URL

To use the username_enum tool:
_python osintforge.py -m username_enum -t <username>_

	-t specifies the username to search for