import argparse
from modules import dns_lookup, metadata_extraction

def main():
    parser = argparse.ArgumentParser(description="OSINTForge - Modular OSINT Tool")
    parser.add_argument('-m', '--module', type=str, required=True, help="Module to run (e.g., dns_lookup, metadata_extraction)")
    parser.add_argument('-t', '--target', type=str, required=True, help="Target for the module (e.g., example.com or file path)")
    args = parser.parse_args()

    if args.module == 'dns_lookup':
        dns_lookup.run(args.target)
    elif args.module == 'metadata_extraction':
        metadata_extraction.run(args.target)
    else:
        print(f"Module '{args.module}' not found.")

if __name__ == "__main__":
    main()