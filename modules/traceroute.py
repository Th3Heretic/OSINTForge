import subprocess
import platform


def run(target):
    """
    Run a traceroute to the specified target and yield output line-by-line.
    This prevents blocking and allows real-time GUI updates.
    """

    if not target or not isinstance(target, str):
        yield "Invalid target. Please provide a valid IP or domain."
        return

    target = target.strip()
    if not target:
        yield "Empty target provided."
        return

    try:
        system = platform.system().lower()

        if "windows" in system:
            traceroute_cmd = ["tracert", "-h", "15", "-w", "3000", target]
        elif "linux" in system or "darwin" in system:
            traceroute_cmd = ["traceroute", "-m", "15", "-w", "2", target]
        else:
            yield f"Unsupported operating system: {system}"
            return

        process = subprocess.Popen(
            traceroute_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # STREAM OUTPUT LINE BY LINE
        for line in process.stdout:
            yield line.strip()

        process.wait()

        if process.returncode != 0:
            error_output = process.stderr.read().strip()
            if error_output:
                yield f"Traceroute failed: {error_output}"

    except Exception as e:
        yield f"Error running traceroute: {str(e)}"