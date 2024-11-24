import argparse
from modules import dns_lookup

def main():
    parser = argparse.ArgumentParser(description="OSINTForge - Modular OSINT Tool")
    parser.add_argument('-m', '--module', type=str, required=True, help="Module to run (e.g., dns_lookup)")
    parser.add_argument('-t', '--target', type=str, required=True, help="Target for the module (e.g., example.com)")
    args = parser.parse_args()

    if args.module == 'dns_lookup':
        dns_lookup.run(args.target)
    else:
        print(f"Module '{args.module}' not found.")

if __name__ == "__main__":
    main()