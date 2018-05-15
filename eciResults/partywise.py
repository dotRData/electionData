import csv
import urllib2
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
from time import sleep
import sys

url = 'http://eciresults.nic.in/PartyWiseResult.htm'

req = urllib2.urlopen(url)
result = req.read()
req.close()
currTime    = str(datetime.now())
parsed_html = BeautifulSoup(result, "html.parser")
table       = parsed_html.find('div', {'id': 'div1'})
states      = table.find_all('table', {'border': '1'})

print('stateName,party,won,leading,total,currTime')
for state in states:
    rows = state.find_all('tr')
    for i in xrange(len(rows)-3):
        if(i == 0): stateName = str(rows[i].text.strip().split(u'\xa0')[0])
        elif(i == 1): continue
        elif(i == 2): continue
        elif(i > 2):
            columnValue = rows[i].find_all('td')
            columnValue = [str(j.text.strip()) for j in columnValue]
            columnValue = ','.join(columnValue)
            print(stateName + ',' + columnValue + ',' + currTime)
