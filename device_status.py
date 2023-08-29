import csv
from datetime import datetime, timedelta

# Input and output file names
input_filename = 'output.csv'
output_filename = 'report_device_status.csv'

# Function to parse the timestamp string to a datetime object
def parse_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

# Initialize variables for the previous timestamp and value
prev_timestamp = None

# Open the input and output files
with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
    # Create CSV readers and writers
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    # Read and skip the header row
    header = next(reader)
    
    # Write the header to the output file
    writer.writerow(header)
    
    for row in reader:
        timestamp_str = row[0]
        
        # Check if the row starts with "Time"; skip it
        if timestamp_str == 'Time':
            continue
        
        current_timestamp = parse_timestamp(timestamp_str)
        
        # Check if the time difference is greater than 3 seconds
        if prev_timestamp is not None and (current_timestamp - prev_timestamp) > timedelta(seconds=3):
            # Write the row to the report file
            writer.writerow(row)
        
        prev_timestamp = current_timestamp
