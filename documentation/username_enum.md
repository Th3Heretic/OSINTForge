# Username Enumeration

## Description

The Username Enumeration module checks whether a given username exists across multiple online platforms.

It performs HTTP-based checks against known platform URL patterns and classifies results based on confidence, helping reduce false positives and improve clarity.

---

## How It Works

The module:

1. Accepts a username as input  
2. Constructs platform-specific profile URLs  
3. Sends HTTP requests to each platform  
4. Analyses responses based on:
   - HTTP status codes  
   - Page content  
   - Final resolved URLs  
5. Classifies results into confidence categories  
6. Executes checks using multi-threading for improved performance  

---

## Result Classification

Results are grouped into three categories:

### Confirmed Matches
- HTTP 200 response  
- Username detected in page content and/or URL  
- High confidence that the username exists  

### Possible Matches / Manual Review
- HTTP 200 with weak or ambiguous indicators  
- Access restricted (e.g. 401, 403, anti-bot responses)  
- May require manual verification  

### Errors / Blocked
- SSL issues, timeouts, or request failures  
- Platform blocking or rate limiting  

A final summary provides counts for each category, including total sites checked.

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "Username Enumeration"  
3. Enter a username  
4. Click "Run Username Enumeration"  

---

### CLI

python osintforge.py -m username_enum -t exampleuser

---

## Example Output

Checking username: exampleuser  

[Confirmed Matches]  
GitHub: https://github.com/exampleuser  
Reddit: https://www.reddit.com/user/exampleuser  

[Possible Matches / Manual Review]  
Instagram: https://www.instagram.com/exampleuser (Access restricted)  

Summary: 2 confirmed, 1 possible, 0 errors, 22 sites checked  

---

## Common Use Cases

- Investigating digital identity across platforms  
- Linking accounts belonging to the same individual  
- Supporting OSINT profiling and attribution  
- Identifying presence on social or developer platforms  

---

## Limitations

- Some platforms use anti-bot protection or return misleading responses  
- A HTTP 200 response does not always guarantee account existence  
- Username matching relies on page content and URL patterns  
- Results may vary depending on platform behaviour and rate limiting  

---

## Future Improvements

- Username variation handling (case changes, symbols, substitutions)  
- Platform-specific parsing for improved accuracy  
- Integration with official APIs where available  
- CSV/JSON export support  
- Confidence scoring system  

---

## Ethical Considerations

Username enumeration should only be conducted for legitimate and authorised purposes.

Care must be taken to avoid profiling or targeting individuals without consent, and to comply with applicable privacy laws and regulations.