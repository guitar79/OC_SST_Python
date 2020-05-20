# Based on python2

import http.client
import time
from datetime import date, timedelta

# Example file path : 
# http://222.236.46.45/nfsdb/COMS/GOCI/1.0/2011/04/01/L1B/COMS_GOCI_L1B_GA_20110401001641.he5.zip

headers = {'User-agent': 'Python'}
conn = http.client.HTTPConnection('222.236.46.45')

baseurl = [
'COMS/GOCI/1.0/',
'COMS/GOCI/1.2/',
'COMS/GOCI/1.3/',
'MODISA/',
'MODIST/',
'NOAA/',
'NPP/',
]
baseurl = [
'MODISA/',
'MODIST/',
]

level = [
#'L1B/',
'L2/',
#'L3/',
]


start_date = date(2016,1,1)
end_date = date(2018,12,31)
delta = end_date - start_date
f = open('list_new.txt', 'w')


# from sys import argv
# script, starttime, endtime, hourgap = argv # Input : starttime, endtime in '20160901'-like format
# start_t = time.strptime(starttime, '%Y%m%d')
# end_t = time.strptime(endtime, '%Y%m%d')
# start_date = date(start_t.tm_year, start_t.tm_mon, start_t.tm_mday)
# end_date = date(end_t.tm_year, end_t.tm_mon, end_t.tm_mday)
# delta = end_date - start_date
duration = delta.days


for i in range(0, len(baseurl)): # for each baseurl
    index_day = 0
    while(index_day <= duration):
        date_now = start_date + timedelta(index_day)
        j = 0
        while(j < len(level)): # for each type
            #try:
            directory = '/nfsdb/' + baseurl[i] + date_now.strftime('%Y') + '/' + date_now.strftime('%m') + '/' + date_now.strftime('%d') + '/' + level[j]
            print ('Parsing ' + directory + '...')
            conn.request('GET', directory, '', headers)
            resp = conn.getresponse()
            print ('debug #1')
            html = resp.read()
            html_split = html.split('HREF="')
            for num_file in range(2, len(html_split)):
                filename = '<' + html_split[num_file].split('.zip')[0] + '.zip' + '>\n'
                print (filename)
                f.write(filename)
            j += 1 # move to next index only if parsing had suceeded
            #except:
            print('404 Not Found')
            
        index_day += 1 # move to next index only if parsing had suceeded