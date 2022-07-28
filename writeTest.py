import json
import requests
import pandas as pd
from pathlib import Path
from openpyxl.workbook import Workbook
import csv



url = 'https://raw.githubusercontent.com/vanceazer/vehicleMediaUpload/main/vdata1.json'
r = requests.get(url)
df = pd.DataFrame(r.json())
df_id = df['id']
# print(df)




def listtostring(lst):
    emptystr = ""

    for ele in lst:
        emptystr = ele

    return emptystr


def writetocsv(items):

    excel_header = ["url", "regnumber", "publicId"]
    data = [[items, mediaUrl, regNumber, publicId]]
    print(data)
    with open('writetestdata.csv', 'a', newline='') as csv_1:
        csv_out = csv.writer(csv_1)
        csv_out.writerows([data[index]] for index in range(0, len(data)))



for items in df_id.values:
    print('-------------------------------')
    print(items)
    media_match = df[df['id'] == items]
    mediaUrl = listtostring(media_match['imageUrl'])
    print(mediaUrl)
    publicId = listtostring(media_match['publicId'])
    print(publicId)
    regNumber = listtostring(media_match['regNumber'])
    print(regNumber)
    print('-------------------------------')
    writetocsv(items)

