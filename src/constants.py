from openpyxl import load_workbook  # pip install openpyxl

DRIVER_PATH = "tools/chromedriver.exe"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
EXCEL_FILE_LOCATION = "search/search.xlsx"
WB = load_workbook(EXCEL_FILE_LOCATION)
WS = WB.active
