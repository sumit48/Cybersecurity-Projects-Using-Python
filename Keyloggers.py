import psutil

# List of known keylogger process names (can be expanded)
KNOWN_KEYLOGGERS = [
    "keylogger.exe", "logkeys", "hooker", "spyware", "winlogon.exe",
    "klog.exe", "keyhook", "iSpy", "GhostLogger"
]

def detect_keyloggers():
    suspicious_processes = []

    # Iterate through all running processes
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            if any(keylogger in process_name for keylogger in KNOWN_KEYLOGGERS):
                suspicious_processes.append((process.info['pid'], process_name))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # Show detected keyloggers or a message if none were found
    if suspicious_processes:
        print("[!] Suspicious keylogger processes detected:")
        for pid, name in suspicious_processes:
            print(f"    PID: {pid} | Process Name: {name}")
    else:
        print(" No known keylogger processes detected.")

if __name__ == "__main__":
    input("Press Enter to begin scanning for keyloggers...")
    print("Scanning for keyloggers...")
    detect_keyloggers()
