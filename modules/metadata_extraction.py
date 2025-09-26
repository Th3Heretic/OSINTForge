"""
metadata_extraction.py

Uses ExifTool to extract metadata from a given file.
Intended for ethical use in controlled environments only.
"""

import os
import subprocess

def run(target):
    print(f" - Extracting metadata from: {target}")

    try:
        # Check if the target is a valid file
        if not os.path.exists(target):
            print(f" - Error: File not found - {target}")
            return

        # Use ExifTool to extract metadata
        command = ["exiftool", target]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Check if any metadata was found
            if result.stdout.strip():
                print(" - Metadata Extraction Results:\n")
                print(f" - {result.stdout}")
            else:
                print(" - No metadata found in the file.")
        else:
            # Print error message if ExifTool failed
            print(f" - Error: {result.stderr}")
    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f" - Error during metadata extraction: {e}")