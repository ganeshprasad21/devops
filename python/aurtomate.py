import subprocess,os

result = subprocess.run(["ls", "-l"],text=True, capture_output=True)
print(result.stdout)  # Output of the command

os.system("ls -lart")

#/home/g/Documents/devops/python/example.json

import json

# Open and read the JSON file
with open("/home/g/Documents/devops/python/example.json", "r") as file:
    data = json.load(file)  # Converts JSON to a Python dictionary
    # datas = json.loads(file)

# Access values
print(data["name"])      # G*
print(data["age"])       # 25
print(data["skills"])    # ['Python', 'Django']

print(data)

data = {
    "name": data["name"]*2 if len(data["name"]*2) < 10 else "G",
    "age": 30,
    "skills": ["JavaScript", "React"],
    "is_employed": False
}
with open("/home/g/Documents/devops/python/example.json", "w") as file:
    json.dump(data, file, indent=4)  # Pretty-print with indentation


import time

def tail_log(file_path):
    """Monitor a log file in real time, similar to `tail -f`."""
    try:
        with open(file_path, "r") as file:
            # Move to the end of the file
            # file.seek(0, 2)
            
            while True:
                line = file.readline()
                if line:
                    print(line.strip())  # Print new log lines
                else:
                    time.sleep(0.5)  # Wait before checking for new lines
    except FileNotFoundError:
        print(f"Error: File {file_path} not found!")
    except KeyboardInterrupt:
        print("\nStopped monitoring.")

if __name__ == "__main__":
    log_file = "/var/log/syslog"  # Change this to your log file path
    tail_log(log_file)

