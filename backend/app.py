from flask import Flask, jsonify, render_template
import requests
from pyxlsb import open_workbook
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Fetch data from XLSB file
    xlsb_url = 'https://vipunen.fi/fi-fi/_layouts/15/XlFileHandler.aspx?id=https%3A%2F%2Fvipunen.fi%2Ffi-fi%2FRaportit%2FAmmatillinen%20koulutus%20-%20ty%C3%B6llistyminen%20ja%20jatko-opinnot%20-%20tilastovuosi.xlsb&sessionId=36.edd378bf-313d-4c32-844d-f4b1d6cd1e7f1.A94.1.V26.173818lMiKxu8mOu7coiU%2BVNIG14.5.fi-FI5.fi-FI36.94153f1a-692f-42fe-a1a9-766f6877aa181.A1.N&workbookFileName=Ammatillinen%20koulutus%20-%20ty%C3%B6llistyminen%20ja%20jatko-opinnot%20-%20tilastovuosi.xlsb&workbookType=PublishedItemsSnapshot'
    data = fetch_data_from_xlsb(xlsb_url)
    return render_template('index.html', data=data)

def fetch_data_from_xlsb(url):
    response = requests.get(url)
    data = []
    if response.status_code == 200:
        workbook = open_workbook(BytesIO(response.content))
        excluded_sheets = ["Raporttiselite", "Graafi", "Ohjeet"]  # Add the sheets you want to exclude
        for sheet_name in workbook.sheets:
            if sheet_name in excluded_sheets:
                continue  # Skip excluded sheets
            sheet_data = []
            for row in workbook.get_sheet(sheet_name).rows():
                row_data = [2 if (isinstance(cell.v, int) and cell.v in range(1, 5)) or (isinstance(cell.v, str) and cell.v == '1-4') else cell.v for cell in row if cell.v is not None]
                if row_data:
                    sheet_data.append(row_data)
            data.append({'sheet_name': sheet_name, 'sheet_data': sheet_data})
    return data

if __name__ == '__main__':
    app.run(debug=True)
