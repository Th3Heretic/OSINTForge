import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from io import StringIO
import sys

# Traceroute import
from traceroute import run as traceroute_run

# WHOIS Lookup import
from whois_lookup import run as whois_lookup_run

# Import the directory scanner's run function
from directory_scanner import run as directory_scan_run
from dns_lookup import run as dns_lookup_run
from email_validation import run as email_validation_run
from ip_geolocation import run as ip_geolocation_run
from metadata_extraction import run as metadata_extraction_run
from port_scanner import run as port_scanner_run
from reverse_dns import run as reverse_dns_run
from ssl_certificate import run as ssl_certificate_run
from subdomain_enum import run as subdomain_enum_run
from username_enum import run as username_enum_run
from website_metadata import run as website_metadata_run

class OSINTForgeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OSINTForge - Open Source Intelligence Toolkit")
        self.root.geometry("800x600")

        # Header area (logo/title)
        header = tk.Frame(self.root, bg="#2c3e50", height=60)
        header.pack(side=tk.TOP, fill=tk.X)
        title = tk.Label(header, text="OSINTForge", fg="white", bg="#2c3e50", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # Main container frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.show_home_screen()

    def show_home_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Scrollable Canvas Setup
        canvas = tk.Canvas(self.main_frame)
        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Title
        intro = tk.Label(scrollable_frame, text="Welcome to OSINTForge\nSelect a module to begin", font=("Arial", 14))
        intro.grid(row=0, column=0, columnspan=3, pady=20)

        # Optional image
        try:
            self.module_icon = tk.PhotoImage(file="media/button_bg.png")
        except Exception:
            self.module_icon = None

        # Button Configuration
        buttons = [
            ("Directory Scanner", self.show_directory_scanner),
            ("DNS Lookup", self.show_dns_lookup),
            ("Email Validation", self.show_email_validation),
            ("IP Geolocation", self.show_ip_geolocation),
            ("Metadata Extraction", self.show_metadata_extraction),
            ("Port Scanner", self.show_port_scanner),
            ("Reverse DNS", self.show_reverse_dns),
            ("SSL Certificate", self.show_ssl_certificate),
            ("Subdomain Enumeration", self.show_subdomain_enumeration),
            ("Traceroute", self.show_traceroute),
            ("Username Enumeration", self.show_username_enum),
            ("Website Metadata", self.show_website_metadata),
            ("WHOIS Lookup", self.show_whois_lookup),
        ]

        for index, (text, command) in enumerate(buttons):
            row = index // 3 + 1
            col = index % 3
            button = tk.Button(
                scrollable_frame,
                text=text,
                width=24,
                height=4,
                compound=tk.LEFT,
                image=self.module_icon,
                command=command
            )
            button.grid(row=row, column=col, padx=10, pady=10)


    def show_whois_lookup(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Domain or IP:").pack(side=tk.LEFT)
        self.whois_entry = tk.Entry(input_frame, width=50)
        self.whois_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run WHOIS Lookup", command=self.run_whois_lookup).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.whois_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.whois_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_whois_lookup(self):
        target = self.whois_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a domain or IP address.")
            return

        self.whois_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        try:
            print(whois_lookup_run(target))
        except Exception as e:
            print(f"[ERROR] WHOIS Lookup failed: {e}")
        finally:
            sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.whois_output_box.insert(tk.END, output)


    def show_website_metadata(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target URL:").pack(side=tk.LEFT)
        self.website_meta_entry = tk.Entry(input_frame, width=50)
        self.website_meta_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Website Metadata", command=self.run_website_metadata).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.website_meta_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.website_meta_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_website_metadata(self):
        target = self.website_meta_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        self.website_meta_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        try:
            website_metadata_run(target)
        except Exception as e:
            print(f"[ERROR] Website metadata extraction failed: {e}")
        finally:
            sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.website_meta_output_box.insert(tk.END, output)


    def show_username_enum(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target Username:").pack(side=tk.LEFT)
        self.username_entry = tk.Entry(input_frame, width=50)
        self.username_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Username Enumeration", command=self.run_username_enum).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.username_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.username_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_username_enum(self):
        target = self.username_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a username.")
            return

        self.username_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        try:
            username_enum_run(target)
        except Exception as e:
            print(f"[ERROR] Username Enumeration failed: {e}")
        finally:
            sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.username_output_box.insert(tk.END, output)


    def show_directory_scanner(self):
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target URL:").pack(side=tk.LEFT)
        self.target_entry = tk.Entry(input_frame, width=50)
        self.target_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Directory Scan", command=self.run_directory_scan).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Export as CSV", command=self.export_results).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_directory_scan(self):
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a target URL.")
            return

        self.output_box.delete("1.0", tk.END)
        self.scan_results = []

        # Capture stdout
        buffer = StringIO()
        sys.stdout = buffer
        directory_scan_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.output_box.insert(tk.END, output)

        # Basic CSV-ready parsing (status lines)
        for line in output.splitlines():
            if " - " in line and line.startswith("http"):
                parts = line.split(" - ")
                self.scan_results.append(parts)


    def export_results(self):
        if not self.scan_results:
            messagebox.showinfo("Info", "No scan results to export.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
            title="Save scan results"
        )
        if file_path:
            with open(file_path, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["URL", "Status"])
                for row in self.scan_results:
                    writer.writerow(row)
            messagebox.showinfo("Exported", f"Results saved to:\n{file_path}")


    def show_dns_lookup(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target URL:").pack(side=tk.LEFT)
        self.dns_entry = tk.Entry(input_frame, width=50)
        self.dns_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run DNS Lookup", command=self.run_dns_lookup).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.dns_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.dns_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_dns_lookup(self):
        target = self.dns_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a domain.")
            return

        self.dns_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        dns_lookup_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.dns_output_box.insert(tk.END, output)


    def show_email_validation(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target Email:").pack(side=tk.LEFT)
        self.email_entry = tk.Entry(input_frame, width=50)
        self.email_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Email Validation", command=self.run_email_validation).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.email_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.email_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_email_validation(self):
        target = self.email_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter an email address.")
            return

        self.email_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        email_validation_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.email_output_box.insert(tk.END, output)


    def show_ip_geolocation(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target IP:").pack(side=tk.LEFT)
        self.ip_entry = tk.Entry(input_frame, width=50)
        self.ip_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run IP Geolocation", command=self.run_ip_geolocation).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.ip_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.ip_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_ip_geolocation(self):
        target = self.ip_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter an IP address.")
            return

        self.ip_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        ip_geolocation_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.ip_output_box.insert(tk.END, output)


    def show_metadata_extraction(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        file_frame = tk.Frame(self.main_frame)
        file_frame.pack(pady=10)
        tk.Label(file_frame, text="Select File:").pack(side=tk.LEFT)
        self.meta_file_path = tk.Entry(file_frame, width=50)
        self.meta_file_path.pack(side=tk.LEFT, padx=5)
        tk.Button(file_frame, text="Browse", command=self.browse_metadata_file).pack(side=tk.LEFT)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Metadata Extraction", command=self.run_metadata_extraction).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.meta_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.meta_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def browse_metadata_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.meta_file_path.delete(0, tk.END)
            self.meta_file_path.insert(0, file_path)


    def run_metadata_extraction(self):
        path = self.meta_file_path.get().strip()
        if not path:
            messagebox.showerror("Error", "Please select a file.")
            return

        self.meta_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        metadata_extraction_run(path)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.meta_output_box.insert(tk.END, output)


    def show_port_scanner(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target Host IP:").pack(side=tk.LEFT)
        self.port_target_entry = tk.Entry(input_frame, width=50)
        self.port_target_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Port Scan", command=self.run_port_scanner).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.port_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.port_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_port_scanner(self):
        target = self.port_target_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a hostname or IP address.")
            return

        self.port_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        port_scanner_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.port_output_box.insert(tk.END, output)


    def show_reverse_dns(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target IP:").pack(side=tk.LEFT)
        self.reverse_dns_entry = tk.Entry(input_frame, width=50)
        self.reverse_dns_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Reverse DNS", command=self.run_reverse_dns).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.reverse_dns_output = tk.Text(self.main_frame, wrap=tk.WORD)
        self.reverse_dns_output.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_reverse_dns(self):
        target = self.reverse_dns_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter an IP address.")
            return

        self.reverse_dns_output.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        reverse_dns_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.reverse_dns_output.insert(tk.END, output)


    def show_ssl_certificate(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target URL:").pack(side=tk.LEFT)
        self.ssl_entry = tk.Entry(input_frame, width=50)
        self.ssl_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run SSL Lookup", command=self.run_ssl_certificate).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.ssl_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.ssl_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_ssl_certificate(self):
        target = self.ssl_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a domain.")
            return

        self.ssl_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        ssl_certificate_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.ssl_output_box.insert(tk.END, output)


    def show_subdomain_enumeration(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target Domain:").pack(side=tk.LEFT)
        self.subdomain_entry = tk.Entry(input_frame, width=50)
        self.subdomain_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Subdomain Enumeration", command=self.run_subdomain_enum).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.subdomain_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.subdomain_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_subdomain_enum(self):
        target = self.subdomain_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a domain.")
            return

        self.subdomain_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        subdomain_enum_run(target)
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.subdomain_output_box.insert(tk.END, output)


    def show_traceroute(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Target Host/IP:").pack(side=tk.LEFT)
        self.traceroute_entry = tk.Entry(input_frame, width=50)
        self.traceroute_entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()
        tk.Button(button_frame, text="Run Traceroute", command=self.run_traceroute).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back to Home", command=self.show_home_screen).pack(side=tk.LEFT, padx=5)

        self.traceroute_output_box = tk.Text(self.main_frame, wrap=tk.WORD)
        self.traceroute_output_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


    def run_traceroute(self):
        target = self.traceroute_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a target host or IP.")
            return

        self.traceroute_output_box.delete("1.0", tk.END)
        buffer = StringIO()
        sys.stdout = buffer
        try:
            traceroute_run(target)
        except Exception as e:
            print(f"[ERROR] Traceroute failed: {e}")
        finally:
            sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        self.traceroute_output_box.insert(tk.END, output)


if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = OSINTForgeGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"[FATAL] GUI failed to launch: {e}")