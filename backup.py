import subprocess
import datetime

def backup_directory(source_dir, destination, is_remote=False):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = f"backup_{timestamp}"
    report_file = "backup_report.txt"
    
    # Prepare rsync command
    rsync_command = ["rsync", "-avz", "--progress", source_dir, destination + "/" + backup_dir]
    
    if is_remote:
        rsync_command.insert(1, "-e")
        rsync_command.insert(2, "ssh")
    
    # Execute rsync command
    try:
        subprocess.run(rsync_command, check=True)
        report = "Backup successful"
    except subprocess.CalledProcessError as e:
        report = f"Backup failed: {str(e)}"

    # Write report to file
    with open(report_file, "w") as f:
        f.write(report)

    print(report)

# Example usage
source_directory = "/path/to/source"
destination_directory = "/path/to/destination"
is_remote_backup = False  # Set to True if destination is a remote server

backup_directory(source_directory, destination_directory, is_remote_backup)

""" 
In this script: backup_directory() function takes three parameters: source_dir (the directory to be backed up), destination (the backup destination), and is_remote (a boolean indicating whether the destination is a remote server).
It generates a timestamp for the backup directory and constructs the rsync command accordingly.
The rsync command is executed using subprocess.run().
If the backup is successful, it writes "Backup successful" to a report file. If it fails, it writes the error message to the report file.
Finally, it prints the report to the console.
You can customize the source_directory, destination_directory, and is_remote_backup variables according to your specific requirements."""