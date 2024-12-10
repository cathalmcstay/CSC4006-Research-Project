
import subprocess
import time
import socket
import argparse

# Configuration
node4_ip = "192.168.0.122"
energy_server_port = 5000
log_file = "job_log.csv"

# Function to Get Energy from Node 4
def get_energy():
    try:
        with socket.create_connection((node4_ip, energy_server_port), timeout=5) as sock:
            energy = sock.recv(1024).decode().strip()
            return float(energy)
    except socket.error as e:
        print(f"Error connecting to Node 4: {e}")
        return -1

# Function to Run a Job
def run_job(cmd):
    print(f"Starting job: {cmd}")

    # Record Initial Energy
    initial_energy = get_energy()
    if initial_energy == -1:
        print("Failed to get initial energy reading.")
        return

    start_time = time.time()

    # Run the Specified Program
    process = subprocess.Popen(cmd, shell=True)
    process.wait()

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Record Final Energy
    final_energy = get_energy()
    if final_energy == -1:
        print("Failed to get final energy reading.")
        return

    energy_used = max(0, final_energy - initial_energy)

    # Log Results
    with open(log_file, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{cmd},{elapsed_time:.2f},{energy_used:.4f}\n")

    print(f"Job completed in {elapsed_time:.2f} seconds")
    print(f"Energy used: {energy_used:.4f} kWh")

# Argument Parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Submit a job and measure energy consumption.")
    parser.add_argument("program", type=str, help="The command to run the program.")
    parser.add_argument("iterations", type=int, help="Number of iterations used in program.")
    args = parser.parse_args()

    # Ensure Log File Exists
    try:
        open(log_file, "x").write("Timestamp,Command,Time (s),Energy (kWh)\n")
    except FileExistsError:
        pass

    # Run the Job
    job_command = f"{args.program} {args.iterations}"
    run_job(job_command)
