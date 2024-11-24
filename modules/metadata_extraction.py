import os
import subprocess

def run(target):
    print(f"Extracting metadata from: {target}")

    try:
        # Check if the target is a valid file
        if not os.path.exists(target):
            print(f"Error: File not found - {target}")
            return

        # Use ExifTool to extract metadata
        command = ["exiftool", target]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            if result.stdout.strip():
                print("Metadata Extraction Results:\n")
                print(result.stdout)
            else:
                print("No metadata found in the file.")
        else:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"Error during metadata extraction: {e}")