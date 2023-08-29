import csv
import time
import speedtest
from datetime import datetime

def perform_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1024 / 1024  # Convert to Mbps
        upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
        return download_speed, upload_speed, None  # No error, so pass None as the error message
    except Exception as e:
        error_message = f"Error performing speed test: {e}"
        return None, None, error_message

def save_to_csv(file_path, time_value, download_speed, upload_speed, error_message):
    with open(file_path, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([time_value, download_speed, upload_speed, error_message])

if __name__ == "__main__":
    file_path = "speed.csv"
    
    save_to_csv(file_path, "Time", "Download Speed (Mbps)", "Upload Speed (Mbps)", "Error Message")  # Write header
    
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        download_speed, upload_speed, error_message = perform_speed_test()
        if download_speed is not None and upload_speed is not None:
            save_to_csv(file_path, current_time, download_speed, upload_speed, "No error")
            print(f"Saved speeds with time {current_time}, Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps to CSV")
        else:
            save_to_csv(file_path, current_time, 0, 0, error_message)  # Save error message to CSV
            print(f"{error_message} at {current_time}")
        time.sleep(300)  # Wait for 5 minutes before the next speed test
