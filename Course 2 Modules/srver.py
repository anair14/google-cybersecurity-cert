import re
from collections import defaultdict

def summarize_server_log(log_file_path):
    # Define a regular expression pattern to match log entries
    log_entry_pattern = re.compile(r'(\S+) (\S+) (\S+) \[([^]]+)\] "(\S+)" (\d+) (\S+) "([^"]+)" "([^"]+)"')

    # Create a defaultdict to store summary information
    summary = defaultdict(int)

    # Read the log file
    with open(log_file_path, 'r') as log_file:
        # Process each line in the log file
        for line in log_file:
            match = log_entry_pattern.match(line)
            if match:
                # Extract relevant information from the log entry
                ip_address, _, _, timestamp, _, status_code, _, _, _ = match.groups()

                # Update the summary information
                summary['total_requests'] += 1
                summary['status_code_counts'][status_code] += 1
                summary['unique_ip_addresses'].add(ip_address)

    return summary

# Example usage:
log_file_path = './sample/server.log'
log_summary = summarize_server_log(log_file_path)

# Print the summary
print(f"Total Requests: {log_summary['total_requests']}")
print(f"Status Code Counts: {log_summary['status_code_counts']}")
print(f"Unique IP Addresses: {len(log_summary['unique_ip_addresses'])}")
