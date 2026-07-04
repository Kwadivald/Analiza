# Project Documentation

This is a simple markdown-style documentation file. It gives a short overview of the main files in this project and explains how they work together.

## Overview

- This document describes the basic structure and purpose of the files in the project.
- It is not a full reference guide, but a demo version of documentation for quick understanding.

### Files and Purpose 

  - .gitignore - a file which states, which files and directories shouldn't be pushed (or sent away) to git servers.

## Data

  * smog_raw.csv - a basic data file, which is made as a foundation for working and preprocessing data on. The smog_raw.ipynb script does the processing of it.

  * smog_raw2.csv - second basic data file meant for basic merging and data preprocessing for jupyter script. 

  * smog_polishraw.csv - data file with polish characters

  * smog1.csv, smog2.csv, smog3.csv - files made for seeing the shape in which the data is made and think about the way in which preprocess the data

## Scripts

  1. csvdata_downloader - a script for downloading current csv data file from data provider and saving it in "data" directory. For executing should be put in scripts directory and just run. When run, it creates an actual timestamp so a user knows from which hour the data is collected. Then a name "smog + timestamp" is created and file is saved (and there is an information about success or failure). * [04.07.2026] - changed, so firstly is downloaded json file, and then it is changed to csv file type. It is also cleaned of wrong characters. 

  2. smog_raw - jupyter script which manages first, basic data wrangling on smog_raw.csv data file. Saves changed file in "tests" directory, with added timestamp. Adds an area column to the data frame and fills it with two first numbers from postal code. Formats numbers to 1 place after comma. Removes "-" from post code so it can be read as an integer. Checks, if every city is in the Poland area based on max latitude and longitude (N, S, E and W point), and returns, how many are outside these points.

## Scripts_different

  - [x] Backupper - a script to backup all repo data in a directory one level higher. To do this, just put a "backupper.py"  file in any directory (preferably "scripts_different") in repository and run it. It will make a "backup" directory one level higher, make inside a directory named "analiza + actual timestamp" and copy whole repo there.

## How the Files Work Together


## Notes

- This document is intended as a simple, high-level guide.
- For more detailed explanations, inspect each file directly.