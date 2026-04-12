## [DEPRECATED]
# Website Metadata

## Description

The Website Metadata module was originally designed to extract metadata and descriptive information from a target website, such as page titles, headers, and embedded tags.

---

## Status

This module is currently **deprecated**.

It has been removed from the active GUI due to inconsistent behaviour and limited reliability when applied across different websites.

---

## Reason for Deprecation

- Inconsistent results across modern websites  
- Heavy reliance on static HTML parsing  
- Limited value compared to other modules  
- Difficulty handling dynamic or JavaScript-driven content  

Modern web applications often load content dynamically, meaning traditional metadata extraction techniques are no longer reliable.

---

## Previous Functionality

The module previously:

1. Accepted a website URL as input  
2. Sent an HTTP request to retrieve page content  
3. Parsed HTML using a library such as BeautifulSoup  
4. Extracted metadata such as:
   - Page title  
   - Meta description  
   - Keywords  
   - Basic HTML structure  

---

## Limitations

- Unable to process JavaScript-rendered content  
- Dependent on static HTML structure  
- Highly inconsistent across different websites  
- No structured or standardised output  

---

## Future Improvements

- Integration with headless browsers (e.g. Selenium or Playwright)  
- Improved parsing for modern web frameworks  
- Structured output (JSON/CSV)  
- Detection of technologies and frameworks  

---

## Ethical Considerations

Website metadata is publicly accessible, but extraction should still be conducted responsibly.

This module should only be used for authorised analysis and educational purposes.