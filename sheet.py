import csv
import time
import subprocess
import psutil
from datetime import datetime

def get_gpu_ram_utilization():
    result = subprocess.run(['tegrastats', '--listgpu'], stdout=subprocess.PIPE)
    output_lines = result.stdout.decode('utf-8').strip().split('\n')
    
    for line in output_lines:
        if 'GR3D_FREQ' in line:
            tokens = line.split(',')
            for token in tokens:
                if 'RAM' in token:
                    ram_utilization = token.split(':')[1].strip()
                    return ram_utilization
    
    return 'N/A'

def get_core_utilization():
    cpu_percent_per_core = psutil.cpu_percent(percpu=True, interval=1)
    return cpu_percent_per_core

def save_to_csv(file_path, data_row):
    with open(file_path, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data_row)

if __name__ == "__main__":
    file_path = "output.csv"
    
    num_cores = psutil.cpu_count(logical=False)
    header = ["Time", "Value"] + [f"Core {core}" for core in range(num_cores)]
    save_to_csv(file_path, header)  # Write header
    
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        core_utilization = get_core_utilization()
        data_row = [current_time, 1] + core_utilization
        save_to_csv(file_path, data_row)
        print(f"Saved value '1' with time {current_time}, Core Utilization: {core_utilization} to CSV")
        time.sleep(1)