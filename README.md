<h1><b><u>OSINTForge Investigation Tool</u></b></h1>

A brief rundown of the project structure:
OSINTForge/
├── modules/
│   ├── __init__.py          # To mark this as a package
│   └── dns_lookup.py        # First module
├── references.txt           # Sources and methodology documentation
├── osintforge.py            # Main CLI script
├── README.md                # Project overview
├── LICENSE                  # GPL v3 license
└── requirements.txt         # Python dependencies

To use the dns_lookup tool:
_python osintforge.py -m dns_lookup -t example.com_

-m is specifying the module to use
-t specifies the target domain

note: The target should be a domain name, not a full URL.