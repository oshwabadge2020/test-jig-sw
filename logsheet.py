import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

class LogSheet:
	def __init__(self):
		# use creds to create a client to interact with the Google Drive API
		self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
		self.creds = ServiceAccountCredentials.from_json_keyfile_name('../client_secret.json', self.scope)
		self.client = gspread.authorize(self.creds)
		self.sheet = self.client.open("Jig1 Programming Results").sheet1
		pass

	def logResult(self,mac,result):
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		#print (dt_string)
		self.sheet.append_row([str(dt_string),mac,result])
		pass
