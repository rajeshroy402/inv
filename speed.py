import csv
import time
import speedtest
from datetime import datetime

def perform_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    return download_speed, upload_speed

def save_to_csv(file_path, time_value, download_speed, upload_speed):
    with open(file_path, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([time_value, download_speed, upload_speed])

if __name__ == "__main__":
    file_path = "speed.csv"
    
    save_to_csv(file_path, "Time", "Download Speed (Mbps)", "Upload Speed (Mbps)")  # Write header
    
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        download_speed, upload_speed = perform_speed_test()
        save_to_csv(file_path, current_time, download_speed, upload_speed)
        print(f"Saved speeds with time {current_time}, Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps to CSV")
        time.sleep(300)  # Wait for 5 minute before the next speed test

