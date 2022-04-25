from openpyxl import load_workbook  # pip install openpyxl

DRIVER_PATH = "tools/chromedriver.exe"
EXCEL_FILE_LOCATION = "search/search.xlsx"
WB = load_workbook(EXCEL_FILE_LOCATION)
WS = WB.active
