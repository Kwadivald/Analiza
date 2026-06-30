import datetime as dt
import requests
import os

# Link to the csv file

csv_link = "https://public-esa.ose.gov.pl/api/v1/smog/csv"

# Actual timestamp

print("Generating timestamp for the filename...")
ts = dt.datetime.now().strftime("%Y%m%d_%H-%M")

# Create a filename with the timestamp

csv_filename = f"./data/smog_{ts}.csv"
print(f"Created filename: {csv_filename}")

#  Download the csv file and save it with the timestamp in the filename

print(f"Downloading the csv file from {csv_link}...")
response = requests.get(csv_link)
with open(csv_filename, 'wb') as file:
    file.write(response.content)

# Check if the file was downloaded successfully

if os.path.exists(csv_filename):
    print(f"Downloaded and saved the csv file")
    print(f"File saved: {csv_filename}")
else:
    print("Failed to download the csv file.")