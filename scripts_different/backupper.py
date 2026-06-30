import os
import datetime
import shutil

# Create a current timestamp for the backup folder name

ts = datetime.datetime.now().strftime("%Y%m%d_%H-%M")
print(f"Created current timestamp: {ts}") 

# Create the backup folder path

bfpath = f"../backup/analiza_{ts}"
print(f"Creating backup folder: {bfpath}")

# Create the backup folder with the timestamp
os.makedirs(bfpath, exist_ok=True)
print(f"Backup folder created: {bfpath}")

# Copy the contents of the parent directory to the backup folder

print(f"Copying contents of the parent directory to the backup folder: {bfpath}")
shutil.copytree("./", bfpath, dirs_exist_ok=True, )
print(f"Contents copied to backup folder: {bfpath}")
print(os.listdir(f"{bfpath}"))