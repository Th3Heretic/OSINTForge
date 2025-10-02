import subprocess
import platform


def run(target):
    """
    Run a traceroute to the specified target and return the output as a string.
    This function is OS-aware and handles basic error scenarios gracefully.
    """

    if not target or not isinstance(target, str):
        return "Invalid target. Please provide a valid IP or domain."

    target = target.strip()
    if not target:
        return "Empty target provided."

    try:
        system = platform.system().lower()

        if "windows" in system:
            traceroute_cmd = ["tracert", "-h", "15", "-w", "3000", target]
        elif "linux" in system or "darwin" in system:  # Linux and macOS
            traceroute_cmd = ["traceroute", "-m", "15", "-w", "2", target]
        else:
            return f"Unsupported operating system: {system}"

        process = subprocess.Popen(traceroute_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            return f"Traceroute failed:\n{stderr.strip()}"

        return stdout.strip()

    except Exception as e:
        return f"Error running traceroute: {str(e)}"