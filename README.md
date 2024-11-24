<h1><b><u>OSINTForge Investigation Tool</u></b></h1>

A brief rundown of the project structure:
OSINTForge/
├── documentation
│   ├── dns_lookup.txt
│   └── metadata_extraction.txt
├── modules/
│   ├── __init__.py          # To mark this as a package
│   ├── dns_lookup.py        # First module
│   └── metadata_extraction.py
├── references.txt           # Sources and methodology documentation
├── osintforge.py            # Main CLI script
├── README.md                # Project overview
├── LICENSE                  # GPL v3 license
└── requirements.txt         # Python dependencies

Installing the dependencies:
- using the terminal navigate to the project folder
- run >ls to check that the requirements.txt is present
- run:
>pip install -r requirements.txt

To use the dns_lookup tool:
_python osintforge.py -m dns_lookup -t example.com_

-m is specifying the module to use
-t specifies the target domain

note: The target should be a domain name, not a full URL.