import os

# List all files with the ".txt" extension in the current directory
txt_files = [f for f in os.listdir(".") if f.endswith(".c")]
print(txt_files)