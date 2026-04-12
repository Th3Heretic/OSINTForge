# Metadata Extraction

## Description

The Metadata Extraction module retrieves embedded metadata from files using ExifTool.

It supports a wide range of file types, including images, documents, and media files, and provides detailed information such as timestamps, device data, and file attributes.

---

## How It Works

The module:

1. Accepts a file path as input  
2. Verifies that the file exists locally  
3. Executes the bundled ExifTool binary  
4. Parses and displays extracted metadata  

The tool is packaged locally within OSINTForge, removing the need for system-wide installation.

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "Metadata Extraction"  
3. Click "Browse" and select a file  
4. Click "Run Metadata Extraction"  

---

### CLI

python osintforge.py -m metadata_extraction -t C:/path/to/file.jpg

---

## Example Output

Extracting metadata from: image.jpg  

Metadata Extraction Results:

File Name: image.jpg  
File Size: 2.1 MB  
Image Width: 1920  
Image Height: 1080  
Create Date: 2023-08-15 14:32:10  
Camera Model: Canon EOS 80D  

---

## Supported File Types

- Images (JPEG, PNG, TIFF, etc.)  
- Documents (PDF, DOCX)  
- Audio/Video files  
- Many other formats supported by ExifTool  

---

## Dependencies

- ExifTool (bundled with OSINTForge)

No additional installation is required, as the executable is included within the project.

---

## Limitations

- Requires local file access (cannot scan remote files)  
- Metadata availability depends on how the file was created  
- Some files may contain minimal or no metadata  
- Output is dependent on ExifTool capabilities  

---

## Future Improvements

- Structured output (JSON/CSV export)  
- Filtering specific metadata fields  
- Drag-and-drop support in GUI  
- Batch file processing  

---

## Ethical Considerations

Metadata may contain sensitive information such as device details, timestamps, or location data.

This module should only be used on files you are authorised to analyse.

Improper use may result in privacy violations or legal consequences.