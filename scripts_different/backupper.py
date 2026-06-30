import os
import datetime
import shutil

# Create a current timestamp for the backup folder name

ts = datetime.datetime.now().strftime("%Y%m%d_%H-%M")

# Create the backup folder path

bfpath = f"../../backup/analiza_{ts}"
print(f"Creating backup folder: {bfpath}")

# Create the backup folder with the timestamp

os.mkdir(bfpath)

# Copy the contents of the parent directory to the backup folder

shutil.copytree("../", bfpath, dirs_exist_ok=True)