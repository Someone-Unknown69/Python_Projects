import datetime

# Define the file path
file_path = "task_scheduler_test.txt"

# Get the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to the file
with open(file_path, "a") as f:
    f.write(f"Task ran at: {current_time}\n")

print(f"✅ Task executed at {current_time}, check the text file!")
