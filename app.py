import subprocess

# Run system commands
memory = subprocess.check_output("free -h", shell=True).decode()
processes = subprocess.check_output("ps aux", shell=True).decode()
block_devices = subprocess.check_output("lsblk", shell=True).decode()

# Combine everything into one output string
output = f"Free Memory:\n{memory}\n\nRunning Processes:\n{processes}\n\nBlock Devices:\n{block_devices}"

# Print the output (this will be shown when the container runs)
print(output)
