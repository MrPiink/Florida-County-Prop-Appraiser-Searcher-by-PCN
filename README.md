# Parcel Number Search for Property Appraisers in Florida

## Description
This project pulls parcel control numbers from an excel spreadsheet given by the user. Then it looks those pcn's up on their corresponding county's property appraiser website. Finally it compares the owner names pulled from the property appraiser and compares them to the owner name attached to each pcn looked up. The result is a log file with all of the matches and non-matches as well as the cells in the spreadsheet being highlighted red or green accordingly.

## Installation
1. Make sure you are using Windows 7 or above.
2. Python 3.8.10 - 13 is required to run.
3. Download all the files in the repository into a singular folder.
4. Use the package manager pip to install requirements.txt
```bash
pip install -r requirements.txt
```
5. Download and install [chrome driver](https://chromedriver.chromium.org/downloads). Then move chromedriver.exe to the tools folder.

## Usage
1. Take the spreadsheet with all of the pcn's being looked up and make sure the pcn's are on column 16. Make sure the first names are on column 4 and last names are on column 3. If there are rows that do not contain a pcn make sure it is filtered out and copy and paste all of the rows with pcn's to a new spreadsheet.
2. Then save the spreadsheet as search.xlsx in the search folder.
3. Edit the config.yml file and change the row start and row end for each county depending on what rows the counties start and end in the spreadsheet.
4. Change the False value to True for all of the counties you wish to check. It is recommended that you only set one county to True at a time. Although, they can all be ran at once.
5. Run main.py. The terminal will display the status of the program since all of the searching will be done on chrome headless mode except for Orange County. During the time Orange County is being searched the computer will be unusable.
6. If you are running each county one at a time make sure to turn that county back to False before running the program for the next county.
7. Once all the counties you need searched have been finished all cells in excel highlighted red were not matches and can be completely ignored.
8. All counties highlighted green must be checked. This can be done by navigating to the logs folder and then to the success logs folder. The success logs in this folder will contain all the information needed for a human to verify whether or not the matches are actual matches. 
9. If they are not matches then best practice is for that corresponding row to be highlighted red by the user.
10. For reuse with a new spreadsheet the search.xlsx should be deleted and the full logs and success logs should have their contents cleared.