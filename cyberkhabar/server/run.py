import subprocess

# Define the paths to the Python files you want to run
file1 = "main.py"
file2 = "file.py"

# Start the first process
process1 = subprocess.Popen(["python", file1])

# Start the second process
process2 = subprocess.Popen(["python", file2])

# Wait for both processes to complete
process1.wait()
process2.wait()