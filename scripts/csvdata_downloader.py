import datetime as dt
import requests
import os
import pandas as pd
import json

# Actual timestamp

print("Generating timestamp for the filename...")
ts = dt.datetime.now().strftime("%Y%m%d_%H-%M")

# Create a filename with the timestamp

csv_filename = f"./data/smog_{ts}.csv"
json_filename = f"./data/smog_{ts}.json"
print(f"Created filename: {json_filename}")
    
# Function cleaning json file and validating it as csv

def json_cleaner(json_filename, csv_filename):
    print("Starting file cleaning")

    # Transfer json to csv for easier cleaning

    df_json = pd.read_json(json_filename, encoding='utf-8-sig')
    df_json.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    df_json = pd.read_csv(csv_filename, encoding='utf-8-sig')
    print("Converting downloaded json to csv file")

    # Drop unnecessary columns

    df_json = df_json.drop(columns=['it_has_next_page', 'pages_total'])
    print("Removing unnecessary columns")

    # List of columns in file

    headlist = [
        "\'name\': ",
        " \'street\':",
        " \'post_code\':",
        " \'city\':",
        " \'longitude\':",
        " \'latitude\':",
        " \"humidity_avg\":",
        " \'pressure_avg\':",
        " \'temperature_avg\':",
        " \'pm10_avg\':", 
        " \'pm25_avg\':",
        " \'timestamp\':"
        ]

    # Remove column names from inside of file

    for x in df_json['smog_data']:
        for y in headlist:
            df_json['smog_data'] = df_json['smog_data'].str.replace(y, "")
    print("Cleaning column names in the file")

    # Clear basic unnecessary chars

    for x in df_json['smog_data']:    
        df_json['smog_data'] = df_json['smog_data'].str.replace("{\'school\': {", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace("}, \'data\': {", ", ")
        df_json['smog_data'] = df_json['smog_data'].str.replace("}", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace("\\t", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace("\\r", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace("\\n", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace(" humidity_avg:", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace("None", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace("\'", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace(",,", "")
        df_json['smog_data'] = df_json['smog_data'].str.replace("\\xa", "")
    print("Cleaning basic unnecessary characters")


    # Save current changes to the temp file

    output = "./temp/smog_jsonclean2.csv"
    input = "./temp/smog_jsonclean.csv"

    print("Saving temporary files")
    df_json.to_csv(input, index=False, encoding='utf-8-sig')
    df_json.to_csv(output, index=False, encoding='utf-8-sig')
    print("Saved temporary files")

    # Remove "\"" characters fom file

    with open(input, 'r', encoding='utf-8-sig') as f:
        with open(output,'w', encoding='utf-8-sig') as ff:
            ff.write(f.read().replace("\"", ""))
    print("Removing \" characters from csv file")

    # Create column names at the top of csv file, add 2 temporary backup columns

    header = "\"NAME\",\"STREET\",\"POST_CODE\",\"CITY\",\"LONGITUDE\",\"LATITUDE\",\"HUMIDITY_AVG\",\"PRESSURE_AVG\",\"TEMPERATURE_AVG\",\"PM10_AVG\",\"PM25_AVG\",\"TIMESTAMP\",\"ERROR1\""

    with open(output, 'r', encoding='utf-8-sig') as f:
        with open(csv_filename,'w', encoding='utf-8-sig') as ff:
            ff.write(f.read().replace("smog_data", header))
    print("Adding column headers + backup error column")

    # Clean columns with coma in "NAME" column
    
    df_csv = pd.read_csv(csv_filename, encoding='utf-8-sig')
    df_csv['ERROR1'] = pd.to_datetime(df_csv['ERROR1'], errors='coerce')
    columns = df_csv.columns[1:]
    for n in columns:
        df_csv[f'{n}'] = df_csv[f'{n}'].astype(str)
    '''for x, y in df_csv['ERROR1'].items():
        if type(y) != type(pd.NaT):
            n = 0
            #df_csv.at[x, 'NAME'] += df_csv.at[x, 'STREET']
            while n < len(columns) - 1 :
                df_csv.at[x, f"'{columns[n]}'"] = df_csv.at[x, f"'{columns[n+1]}'"]
                #print(columns[n], columns[n + 1])
                n += 1
            #print(df_csv.at[x, 'NAME'], df_csv.at[x, 'STREET'])'''
    for x, y in df_csv['ERROR1'].items():
        if type(y) != type(pd.NaT):
            n = 1
            while n + 1 < len(columns) - 1:
                print(n)
                df_csv.iloc[x, n - 1] = df_csv.iloc[x, n]
                #df_csv.replace(df_csv.at[x, f"{columns[n]}"], df_csv.at[x, f"{columns[n + 1]}"])
                #print(f"'{columns[n]}'", df_csv.iloc[x, n])
                n += 1
                #print(type(df_csv.at[x, 'NAME']))
            df_csv.iloc[x, 0] += df_csv.iloc[x, 1]
    df_csv.to_csv("E:/AWDP/Marcia/Analiza/temp/smog_csvclean.csv", index=False, encoding='utf-8-sig')
            
    if os.path.exists(csv_filename):
        print(f"Transferred json to the csv file")
        print(f"File saved: {csv_filename}")
    else:
        print("Failed to transfer into csv file.")
        
    print("Cleaning successful")

# Define function for downloading json file:

def file_downloader():
    # Link to the data file

    json_link = "https://public-esa.ose.gov.pl/api/v1/smog"
    #csv_link = "https://public-esa.ose.gov.pl/api/v1/smog/csv"

    #  Download the  file and save it with the timestamp in the filename

    print(f"Downloading the json file from {json_link}...")
    response = requests.get(json_link)
    with open(json_filename, 'wb') as file:
        file.write(response.content)

    # Check if the file was downloaded successfully. 

    if os.path.exists(json_filename):
        print(f"Downloaded and saved the json file")
        print(f"File saved: {json_filename}")
    else:
        print("Failed to download the json file.")

# Download json file

file_downloader()

# If downloaded file exists, perform cleaning on it and turn into csv file.

json_cleaner(json_filename, csv_filename)