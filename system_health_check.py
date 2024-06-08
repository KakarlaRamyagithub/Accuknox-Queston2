import psutil
import datetime

# Define thresholds
CPU_THRESHOLD = 80  # Percentage
MEMORY_THRESHOLD = 80  # Percentage
DISK_THRESHOLD = 80  # Percentage

# Function to check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        return f"High CPU usage detected: {cpu_usage}%"
    return None

# Function to check memory usage
def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        return f"High memory usage detected: {memory_usage}%"
    return None

# Function to check disk space
def check_disk_space():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        return f"Low disk space detected: {disk_usage}%"
    return None

# Function to check running processes
def check_running_processes():
    num_processes = len(psutil.process_iter())
    return f"Number of running processes: {num_processes}"

# Function to log alerts
def log_alerts(alerts):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_health.log", "a") as f:
        f.write(f"{timestamp} - {', '.join(alerts)}\n")

# Main function
def main():
    alerts = []
    cpu_alert = check_cpu_usage()
    memory_alert = check_memory_usage()
    disk_alert = check_disk_space()
    process_alert = check_running_processes()

    if cpu_alert:
        alerts.append(cpu_alert)
    if memory_alert:
        alerts.append(memory_alert)
    if disk_alert:
        alerts.append(disk_alert)
    if process_alert:
        alerts.append(process_alert)

    if alerts:
        print("System health issues detected:")
        for alert in alerts:
            print(alert)
        log_alerts(alerts)
    else:
        print("System is healthy")

if __name__ == "__main__":
    main()


"""
This script uses the psutil library to retrieve system metrics. Here's a breakdown of how it works:
The script defines thresholds for CPU usage, memory usage, and disk space.
Functions are defined to check each metric against its threshold.
If any metric exceeds its threshold, an alert message is generated.
Alerts are logged to a file named system_health.log.
The main function runs all checks and logs alerts if any are found.
You can adjust the thresholds and customize the alerting mechanism according to your requirements."""