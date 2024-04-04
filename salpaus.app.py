import requests
from pyxlsb import open_workbook
from io import BytesIO

def fetch_and_parse_xlsb(url):
    # Download the XLSB file
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the downloaded data
        workbook = open_workbook(BytesIO(response.content))
        excluded_sheets = ["Raporttiselite", "Graafi", "Ohjeet"]  # Add the sheets you want to exclude
        for sheet_name in workbook.sheets:
            if sheet_name in excluded_sheets:
                continue  # Skip excluded sheets
            sheet = workbook.get_sheet(sheet_name)
            print(f"Sheet: {sheet_name}")
            for row in sheet.rows():
                row_data = [2 if (isinstance(cell.v, int) and cell.v in range(1, 5)) or (isinstance(cell.v, str) and cell.v == '1-4') else cell.v for cell in row if cell.v is not None]  # Replace 1-4 with 2
                if row_data:  # Only print non-empty rows
                    print(row_data)
    else:
        print(f"Failed to download XLSB file from {url}")

# tarvitsee uniikin SESSIONID joka kerta kun käyttäää
xlsb_url = 'https://vipunen.fi/fi-fi/_layouts/15/XlFileHandler.aspx?id=https%3A%2F%2Fvipunen.fi%2Ffi-fi%2FRaportit%2FAmmatillinen%20koulutus%20-%20ty%C3%B6llistyminen%20ja%20jatko-opinnot%20-%20tilastovuosi.xlsb&sessionId=36.edd378bf-313d-4c32-844d-f4b1d6cd1e7f1.D94.1.V26.1371577XE6UkfeCxeD8lMONzz914.5.fi-FI5.fi-FI36.94153f1a-692f-42fe-a1a9-766f6877aa181.A1.N&workbookFileName=Ammatillinen%20koulutus%20-%20ty%C3%B6llistyminen%20ja%20jatko-opinnot%20-%20tilastovuosi.xlsb&workbookType=PublishedItemsSnapshot'
fetch_and_parse_xlsb(xlsb_url)
