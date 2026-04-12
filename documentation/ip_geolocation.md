## **[DEPRECATED]**
# IP Geolocation

## Description

The IP Geolocation module was designed to retrieve approximate geographical information for a given IP address using an external API.

This included details such as country, region, city, and ISP.

---

## Status

This module is currently **deprecated**.

The external API previously used for geolocation is no longer functional or reliable, resulting in inconsistent or failed lookups.

As a result, the module has been removed from the active GUI and is not recommended for use.

---

## Reason for Deprecation

- Dependency on a third-party API that is no longer operational  
- Lack of reliability and consistency in returned data  
- Potential rate-limiting and service restrictions  
- Not aligned with the project's goal of stability and maintainability  

---

## Previous Functionality

The module previously:

1. Accepted an IP address as input  
2. Sent a request to a public geolocation API  
3. Parsed and displayed location-based metadata  

Example data included:

- Country  
- Region  
- City  
- ISP / Organisation  
- Latitude / Longitude  

---

## Limitations

- Fully dependent on external API availability  
- No offline capability  
- Accuracy limited to IP-based estimation (not precise location)  
- Subject to API rate limits and blocking  

---

## Future Improvements

- Replace with a more reliable and documented API  
- Implement fallback providers for redundancy  
- Add local database support (e.g. GeoLite2) for offline use  
- Introduce caching to reduce repeated requests  

---

## Ethical Considerations

IP geolocation provides approximate location data and should not be treated as precise or definitive.

This capability must only be used for legitimate and authorised purposes, such as defensive security analysis or research.

Misuse for tracking or targeting individuals is strongly discouraged.