import gspread
from oauth2client.service_account import ServiceAccountCredentials

class st:
    def __init__(self, ds="PolyCon"):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        self.gc = gspread.authorize(credentials)
        self.ss = ds
    def addWS(self, spreadsheet, name,  head, rows=100):
        sh = self.gc.open(spreadsheet)
        worksheet = sh.add_worksheet(title=name, rows=rows, cols=len(head))
        col = 1
        for rv in head:
            worksheet.update_cell(1, col, rv)
            col += 1
    def addRow(self, spreadsheet, worksheet, row):
        sh = self.gc.open(spreadsheet)
        worksheet = sh.worksheet(worksheet)
        worksheet.append_row(row)