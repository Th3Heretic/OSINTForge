# Directory Scanner

## Description

The Directory Scanner module attempts to identify hidden or unlisted directories on a target website by testing paths from a predefined local wordlist.

The module reports only meaningful results, such as accessible, redirected, unauthorised, or forbidden directories, rather than printing every failed request. This makes the output clearer and more useful during reconnaissance.

---

## How It Works

The module:

1. Accepts a target website as input.
2. Normalises the target so the user can enter a bare domain without needing to include a protocol manually.
3. Loads directory names from a local wordlist stored in the `data` folder.
4. Sends HTTP requests to candidate paths using multi-threaded execution for faster performance.
5. Filters output so only interesting responses are displayed.

The following response types are treated as useful findings:

- `200 OK`
- `301 / 302 / 307 / 308 Redirect`
- `401 Unauthorized`
- `403 Forbidden`

A `403 Forbidden` response is still valuable because it indicates that the directory exists, even if access is denied.

---

## Usage

### GUI

1. Open OSINTForge.
2. Select **Directory Scanner**.
3. Enter a target domain or URL.
4. Click **Run Directory Scan**.

The module accepts input such as:

```bash
example.com
```
or
```bash
https://example.com
```

### CLI
```bash
python osintforge.py -m directory_scanner -t example.com
```

#### Example Output
```
- Scanning directories on: example.com
- Found: http://example.com/admin/ -> 403 Forbidden
- Found: http://example.com/login/ -> 200 OK
- Scan complete. 2 interesting directories discovered.
```
If no useful results are found:
```
- Scanning directories on: example.com
- No interesting directories found.
```

---

## Common Use Cases

- Identifying hidden web resources such as /admin/, /login/, or /backup/
- Detecting misconfigured web directories
- Supporting reconnaissance during authorised security testing
- Mapping visible parts of a target web application

---

## Limitations

- The module uses a static local wordlist and does not currently support custom wordlist selection through the GUI.
- Results depend on the quality and size of the wordlist.
- Some targets may use rate limiting, web application firewalls, or anti-bot protections.
- A directory not shown in the results is not guaranteed not to exist; it may simply not be included in the current wordlist.

---

## Future Improvements

- GUI support for custom wordlist selection
- Export results to additional formats such as JSON
- Adjustable thread count from the interface
- Optional recursive scanning of discovered directories

---

## Ethical Considerations

#### This module should only be used against systems you own or have explicit permission to assess.

#### Unauthorised directory scanning may breach acceptable use policies or UK law, including the Computer Misuse Act 1990.
