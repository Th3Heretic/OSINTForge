import subprocess
import platform

def perform_traceroute(target):
    """Perform a traceroute to the given target with real-time output."""
    try:
        system = platform.system().lower()
        traceroute_cmd = []

        if "windows" in system:
            traceroute_cmd = ["tracert", "-h", "15", "-w", "3000", target]
        elif "linux" in system or "darwin" in system:  # macOS is "Darwin"
            traceroute_cmd = ["traceroute", "-m", "15", "-w", "2", target]
        else:
            return {"error": f"Unsupported operating system: {system}"}

        print(f"Running traceroute: {' '.join(traceroute_cmd)}")

        # Use Popen for real-time streaming of output
        process = subprocess.Popen(traceroute_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Read output line by line
        for line in iter(process.stdout.readline, ""):
            print(line.strip())

        # Wait for process to complete and capture return code
        process.wait()

        if process.returncode != 0:
            return {"error": process.stderr.read().strip()}

        return {"output": "Traceroute completed successfully."}
    except Exception as e:
        return {"error": str(e)}

def run(target):
    """Run the Traceroute module."""
    print(f"Performing traceroute for: {target}")
    result = perform_traceroute(target)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("\nTraceroute Results:")
        print(result["output"])