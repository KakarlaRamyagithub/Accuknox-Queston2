import re
from collections import Counter

# Function to parse log file and extract relevant data
def parse_log(log_file):
    ip_addresses = []
    requested_pages = []
    status_codes = []

    with open(log_file, 'r') as file:
        for line in file:
            parts = re.split(r'\s+', line)
            ip_addresses.append(parts[0])
            requested_pages.append(parts[6])
            status_codes.append(parts[8])

    return ip_addresses, requested_pages, status_codes

# Function to analyze log data and generate report
def analyze_log(ip_addresses, requested_pages, status_codes):
    # Count occurrences of each status code
    status_code_counts = Counter(status_codes)

    # Count occurrences of each IP address
    ip_counts = Counter(ip_addresses)

    # Find the most requested pages
    most_requested_pages = Counter(requested_pages).most_common(5)

    # Find 404 errors
    num_404_errors = status_code_counts.get('404', 0)

    # Find IP address with the most requests
    most_common_ip = ip_counts.most_common(1)

    # Generate report
    report = f"=== Log Analysis Report ===\n\n"
    report += f"Number of 404 errors: {num_404_errors}\n\n"
    report += f"Most requested pages:\n"
    for page, count in most_requested_pages:
        report += f"{page}: {count} requests\n"
    report += f"\nIP address with the most requests: {most_common_ip[0][0]} ({most_common_ip[0][1]} requests)\n"

    return report

# Main function
def main():
    log_file = 'web_server.log'  # Path to your web server log file
    ip_addresses, requested_pages, status_codes = parse_log(log_file)
    report = analyze_log(ip_addresses, requested_pages, status_codes)
    print(report)

if __name__ == "__main__":
    main()


"""
This script performs the following steps:
It reads a web server log file and extracts IP addresses, requested pages, and status codes from each log entry.
It analyzes the extracted data to find the number of 404 errors, the most requested pages, and the IP address with the most requests.
It generates a summarized report containing the analysis results.
Finally, it prints the report to the console.
You can customize the log_file variable to point to your web server log file. Additionally, you can adjust the script to analyze other patterns or generate different types of reports as needed.
"""