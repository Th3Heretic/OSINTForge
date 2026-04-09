<h1><b><u>OSINTForge Investigation Tool</u></b></h1>

Please note, some of these modules aren't perfect and may not work for whatever reason on your system. Also, this is a 
passion project so more updates or modules may be released at a later time but don't expect them to be regular. 

Thanks, and I hope you enjoy using this early access OSINT tool :)

<h2><u>Project structure: </h2></u> 
OSINTForge/ <br>
├── documentation            # Filled with usage documentation for each module <br> 
│   ├── directory_scanner.txt  <br>
│   ├── dns_lookup.txt <br>
│   ├── metadata_extraction.txt<br>
│   ├── port_scanner.txt <br>
│   ├── reverse_dns.txt <br>
│   ├── ssl_certificate.txt <br>
│   ├── reverse_image_search.txt <br>
│   ├── OSINTForge.txt <br>
│   ├── subdomain_enum.txt <br>
│   ├── ip_geolocation.txt <br>
│   ├── website_metadata.txt <br>
│   └── whois_lookup.txt <br>
├── modules/ <br>
│   ├── __init__.py          # To mark this as a package <br>
│   ├── directory_scanner.py # Ninth module <br>
│   ├── dns_lookup.py        # First module <br>
│   ├── email_validation.py  # Eighth module <br>
│   ├── metadata_extraction.py # Second module <br>
│   ├── port_scanner.py      # Sixth module <br>
│   ├── reverse_dns.py       # Eleventh module <br>
│   ├── ssl_certificate.py   # Tenth module <br>
│   ├── subdomain_enum.py    # Fifth module <br>
│   ├── traceroute.py        # Twelfth module <br>
│   ├── ip_geolocation.py    # Third module <br>
│   ├── website_metadata.py  # Seventh module <br>
│   └── whois_lookup.py      # Fourth module <br>
├── references.txt           # Sources and methodology documentation <br>
├── osintforge.py            # Main CLI script <br>
├── README.md                # Project overview <br>
├── LICENSE                  # GPL v3 license <br>
└── requirements.txt         # Python dependencies <br>

<h2><u>Installing the dependencies: </u></h2>
- using the terminal navigate to the project folder
- to check that the requirements.txt is present, run: 
>ls 
- Once you have confirmed its presence in the cwd run:
>pip install -r requirements.txt


To use the <b>dns_lookup</b> tool:
>_python osintforge.py -m dns_lookup -t example.com_

- m is specifying the module to use
- t specifies the target domain

note: The target should be a domain name, not a full URL.


To use the <b>metadata_extraction</b> tool:
>_python osintforge.py -m metadata_extraction -t /absolute/path/to/image.jpg_

- m once again specifies the module
- t is specifying the target image filepath

DEPRECATED
To use the <b>ip_geolocation</b> tool:
_python osintforge.py -m ip_geolocation -t 0.0.0.0_

-t is used to specify a target IP address
-can be used in conjunction with the dns_lookup and subdomain_enum modules


To use the <b>whois_lookup</b> tool:
>_python osintforge.py -m whois_lookup -t example.com_

- t specifies a target domain name


To use the <b>subdomain_enum</b> tool:
>_python osintforge.py -m subdomain_enum -t example.com_

- t specifies a target domain name

To use the <b>port_scanner</b> tool:
>_python osintforge.py -m port_scanner -t 8.8.8.8_

- t specifies a target IP to audit for open ports

DEPRECATED
To use the <b>website_metadata</b> tool:
_python osintforge.py -m website_metadata -t example.com_

-t specifies a domain name

DEPRECATED
To use the email_validation tool:
_python osintforge.py -m email_validation -t email@example.com_

-t specifies an email address

To use the <b>directory_scanner</b> tool:
>_python osintforge.py -m directory_scanner -t https://example.com_

- t specifies a URL to inspect

To use the <b>ssl_certificate</b> tool:
>_python osintforge.py -m ssl_certificate -t example.com_

- t specifies the target URL or IP

To use the <b>reverse_dns</b> tool:
>_python osintforge.py -m reverse_dns -t 8.8.8.8_

- t specifies the IP assigned to a domain

To use the <b>traceroute</b> tool:
>_python osintforge.py -m traceroute -t example.com_

- t specifies a target URL

To use the <b>username_enum</b> tool:
>_python osintforge.py -m username_enum -t <username>_

- t specifies the username to search for

