# Project Documentation

This is a simple markdown-style documentation file. It gives a short overview of the main files in this project and explains how they work together.

## Overview

- This document describes the basic structure and purpose of the files in the project.
- It is not a full reference guide, but a demo version of documentation for quick understanding.

## Files and Purpose


## How the Files Work Together


## Notes

- This document is intended as a simple, high-level guide.
- For more detailed explanations, inspect each file directly.

## Scripts

1. csvdata_downloader - a script for downloading current csv data file from data provider and saving it in "data" directory. For executing should be put in scripts directory and just run. When run, it creates an actual timestamp so a user nows from which hour the data is collected. Then a name "smog + timestamp" is created and file is saved (and there is a information about success or failure).

## Scripts_different

- [x] Backupper - a script to backup all repo data in a directory one level higher. To do this, just put a "backupper.py"  file in any directory (preferably "scripts_different") in repository and run it. It will make a "backup" directory one level higher, make inside a directory named "analiza + actual timestamp" and copy whole repo there.