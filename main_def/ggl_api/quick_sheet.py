from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
import numpy as np
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.80
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    return values

def get_df_from_speadsheet(gsheet_id: str, sheet_name: str):
    # need to optimize to read df from column_index: int = 0 (default = 0)
    data = main()
    column = data[0]
    check_fistrow = data[1]
    x = len(column) - len(check_fistrow)
    k = [None] * x
    check_fistrow.extend(k)  # if only have column name but all data of column null =>> error
    row = data[2:]
    row.insert(0, check_fistrow)
    df = pd.DataFrame(row, columns=column).apply(lambda x: x.str.strip()).fillna(value='').astype(str)
    # df.apply(lambda x: x.str.strip()).fillna(value='').astype(str)
    return df

def createList(r1, r2):
    return list(range(r1, r2+1))

if __name__ == '__main__':
# The ID and range of a sample spreadsheet.one
#     SAMPLE_SPREADSHEET_ID = '15mZzXaSUn6M3gbP4FEFzGDCSox5wx8RG-1NWONo4Ao8'
#     SAMPLE_RANGE_NAME = 'Nov - W4'

    SAMPLE_SPREADSHEET_ID = '1xpFtEI7AhIm5ytc6t1u8DXWOOUTpdjPCKKLND7Hamm4'
    SAMPLE_RANGE_NAME = 'Artist_wiki'

    values = main()
    row_index = values[0]
    length = len(row_index)
    values = [[None if x == '' else x for x in c] for c in values]
    values=np.array([xi+[None]*(length-len(xi)) if (length-len(xi)) >= 0 else xi[0:length] for xi in values],dtype=object)
    axis = 1
    range_list = createList(0,length-1)
    np_array = np.take(values[1:], range_list, axis)
    df2 = pd.DataFrame(np.array(np_array), columns=[row_index])
    print(df2)

    # cannot pass with more than null column tiltle
    df3 = get_df_from_speadsheet(SAMPLE_SPREADSHEET_ID,SAMPLE_RANGE_NAME)
    print(df3)
