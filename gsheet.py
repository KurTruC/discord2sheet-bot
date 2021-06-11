# BSD 3-Clause License
# Copyright (c) 2019, Hugonun(https://github.com/hugonun)
# All rights reserved.

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class gsheet(object):
    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('sheets', 'v4', credentials=self.creds)
    def add(self,sheetid,sheetrange,ivalue):
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        values = []
        values.append(ivalue)
        body = {
            'values': values
        }
        result = sheet.values().append(
            spreadsheetId=sheetid, range=sheetrange,
            valueInputOption='USER_ENTERED', body=body).execute()

    def read(self, sheetid, sheetrange, ivalue):
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        values = []
        values.append(ivalue)
        body = {
             'values': values
        }

        result2 = sheet.values().get(spreadsheetId=sheetid, range=sheetrange).execute()
        values = result2.get('values', [])
        print('{0} rows retrieved.'.format(len(values)))
        #print(result2)

        if not values:
            print('No data found.')
        else:
            #print('Name, Major:') #affichage console
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s, %s' % (row[0], row[1], row[0]))
                #await ctx.send(f"Vous devez attendre {row[0]} ou temps hors-ligne {row[1]}")
        #print(f"Arg0: {args[0]}")


