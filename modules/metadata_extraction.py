"""
metadata_extraction.py

Uses ExifTool to extract metadata from a given file.
Intended for ethical use in controlled environments only.
"""

from __future__ import annotations

import platform
import shutil
import subprocess
from pathlib import Path


def _project_root() -> Path:
    """
    Resolve the project root from this module location.
    Assumes this file lives in OSINTForge/modules/.
    """
    return Path(__file__).resolve().parent.parent


def _get_exiftool_path() -> str | None:
    """
    Return the best available ExifTool path for the current OS.

    Priority:
    1. Bundled Windows executable inside the project
    2. System PATH fallback (useful for macOS/Linux developers)
    """
    root = _project_root()
    system_name = platform.system().lower()

    if system_name == "windows":
        bundled = root / "tools" / "windows" / "exiftool.exe"
        if bundled.is_file():
            return str(bundled)

    # For macOS/Linux, prefer an installed system version
    path_version = shutil.which("exiftool")
    if path_version:
        return path_version

    return None


def run(target: str) -> None:
    """
    Extract metadata from the supplied file path and print results.
    """
    print(f" - Extracting metadata from: {target}")

    try:
        if not target or not str(target).strip():
            print(" - Error: No file selected.")
            return

        file_path = Path(target).expanduser().resolve()

        if not file_path.exists():
            print(f" - Error: File not found - {file_path}")
            return

        if not file_path.is_file():
            print(f" - Error: Target is not a file - {file_path}")
            return

        exiftool_path = _get_exiftool_path()
        if not exiftool_path:
            print(" - Error: ExifTool was not found.")
            print(" - Windows: bundle tools/windows/exiftool.exe with exiftool_files/")
            print(" - macOS/Linux: install ExifTool so 'exiftool' is available on PATH")
            return

        command = [exiftool_path, str(file_path)]
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        if result.returncode == 0:
            if result.stdout.strip():
                print(" - Metadata Extraction Results:\n")
                print(result.stdout)
            else:
                print(" - No metadata found in the file.")
        else:
            stderr = result.stderr.strip() or "Unknown ExifTool error."
            print(f" - Error: {stderr}")

    except Exception as exc:
        print(f" - Error during metadata extraction: {exc}")