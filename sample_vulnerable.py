import subprocess

# Example 1: Hardcoded password
password = "admin123"

# Example 2: Unsafe eval()
def calculate(user_input):
    return eval(user_input)

# Example 3: Unsafe exec()
def execute_code(code):
    exec(code)

# Example 4: Unsafe shell command
def run_command(command):
    subprocess.run(command, shell=True)

print("SAST security testing file")
