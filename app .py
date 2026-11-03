mport subprocess

def run_command():
    print("Welcome to SAST Security Scanner")

    user_input = input("Enter a command: ")

    subprocess.call("echo " + user_input, shell=True)


if __name__ == "__main__":
    run_command()
