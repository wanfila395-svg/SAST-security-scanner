import ast
import sys
from pathlib import Path

def scan_file(file_path):
    print(f"\nScanning: {file_path}")

    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except Exception as error:
        print(f"Could not scan file: {error}")
        return

    for node in ast.walk(tree):

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in ("eval", "exec"):
                    print(
                        f"[WARNING] Dangerous function: "
                        f"{node.func.id}() at line {node.lineno}"
                    )

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id.lower()

                    if any(word in name for word in
                           ("password", "secret", "token", "api_key")):
                        if isinstance(node.value, ast.Constant):
                            if isinstance(node.value.value, str):
                                print(
                                    f"[WARNING] Possible hardcoded "
                                    f"secret at line {node.lineno}"
                                )

        if isinstance(node, ast.keyword):
            if node.arg == "shell":
                if isinstance(node.value, ast.Constant):
                    if node.value.value is True:
                        print(
                            f"[WARNING] shell=True at line {node.lineno}"
                        )


def scan_directory(directory):
    for file_path in Path(directory).rglob("*.py"):
        if any(part in {".git", "venv", "_pycache_"}
               for part in file_path.parts):
            continue

        scan_file(file_path)s


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sast_scanner.py <directory>")
    else:
        scan_directory(sys.argv[1])
