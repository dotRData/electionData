import csv
import urllib2, requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
from time import sleep
import sys

stateCode = '10' #08

# for i in xrange(1,500):
#     url = 'http://eciresults.nic.in/ConstituencywiseS' + stateCode + str(i) + '.htm?ac=' + str(i)
#     request = requests.get(url)
#     print(url)
#     if(len(request.history) == 0): continue
#     else: break

i=225
totalConstituency = i-1
print('no,constiName,candidate,party,votes,currTime')
currTime    = str(datetime.now())
for t in xrange(1, totalConstituency):
    url = 'http://eciresults.nic.in/ConstituencywiseS' + stateCode + str(t) + '.htm?ac=' + str(t)
    req = urllib2.urlopen(url)
    result = req.read()
    req.close()
    parsed_html = BeautifulSoup(result, "html.parser")
    table       = parsed_html.find('div', {'id': 'div1'})
    constis     = table.find_all('table', {'border': '1'})
    for consti in constis:
        rows = consti.find_all('tr')
        for i in xrange(len(rows)):
            if(i == 0): constiName = str(rows[i].text.strip().split(u'\xa0')[0])
            elif(i == 1): continue
            elif(i == 2): continue
            elif(i > 2):
                columnValue = rows[i].find_all('td')
                columnValue = [str(j.text.strip()) for j in columnValue]
                columnValue = ','.join(columnValue)
                print(str(t) + ',' + constiName + ',' + columnValue + ',' + currTime)
