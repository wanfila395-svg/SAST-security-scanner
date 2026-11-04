import re
from pathlib import Path

print("================================")
print("     FILA SAST SECURITY SCANNER")
print("================================")

def scan_file(filename):

    file_path = Path(filename)

    if not file_path.is_file():
        print("File not found!")
        return

    code = file_path.read_text(
        encoding="utf-8",
        errors="replace"
    )

    vulnerabilities = {
        "Command Injection": r"shell\s*=\s*True",
        "Dangerous Evaluation": r"\beval\s*\(",
        "Unsafe Execution": r"\bexec\s*\(",
        "Hardcoded Password": r"password\s*=\s*['\"]"
    }

    print("\nStarting security scan...\n")

    found = False

    for name, pattern in vulnerabilities.items():

        if re.search(pattern, code):

            print("[!] VULNERABILITY:", name)
            found = True

    if not found:
        print("[+] No matching security patterns found.")

    print("\nScan completed.")

if __name__ == "__main__":

    target = input("Enter Python file to scan: ")

    scan_file(target)
