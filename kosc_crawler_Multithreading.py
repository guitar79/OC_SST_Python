"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr

"""
from urllib.request import urlopen
from pathlib import Path

#threading library
import threading

import sys

prefix = 'AWS-01min'

#single thread class
class crawler():
	def __init__(self, year, month, day, hour, minute, threadno):
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.output = ''
		self.threadno = threadno

	def fetch(self):
		my_file = Path('%d/%s_%d%02d%02d%02d%02d.csv' % (self.year, prefix, self.year, self.month, self.day, self.hour, self.minute))
		if my_file.is_file(): # csv file already exists in my folder
			print ('File exists %d/%s_%d%02d%02d%02d%02d.csv' % (self.year, prefix, self.year, self.month, self.day, self.hour, self.minute))
		else:	
			while True:
				try:
					url = "http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?%d%02d%02d%02d%02d&0&MINDB_01M&0&1" % (self.year, self.month, self.day, self.hour, self.minute)
					#open output file
					with open('%d/%s_%d%02d%02d%02d%02d.csv' % (self.year, prefix, self.year, self.month, self.day, self.hour, self.minute), 'w') as f:
						#write
						f.write(self.output)
					break
				except:
					sys.stderr.write("Thread #%d failed...retry\n" % self.threadno)
					pass

#crawler for single month
class crawler_day(threading.Thread):
	def __init__(self, year, month, day, threadno):
		threading.Thread.__init__(self)
		self.year = year
		self.month = month
		self.day = day
		self.threadno = threadno
		sys.stderr.write('Thread #%d started...\n' % (self.threadno))

	def run(self):
		for Ho in range(0, 24):
			for Mn in range(0, 60): 
				fetcher = crawler(self.year, self.month, self.day, Ho, Mn, self.threadno)
				fetcher.fetch()
				sys.stderr.write('Thread #%d - fetched %d-%02d-%02d %02d:%02d...\n' % (self.threadno, self.year, self.month, self.day, Ho, Mn))

threadno = 0
for Yr in range(2011, 2020):
	for Mo in range(1, 13):
		for Da in range(1, 32):
			cmonth = crawler_day(Yr, Mo, Da, threadno)
			cmonth.start()
			threadno += 1



Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@guitar79 
guitar79
/
KOSC_file_downloader
1
0
0
 Code
 Issues 0
 Pull requests 0 Actions
 Projects 0
 Wiki
 Security 0
 Insights
 Settings
KOSC_file_downloader/kosc_crawler_modis_sst.py /
@guitar79 guitar79 Add files via upload
9b2beee 1 minute ago
62 lines (47 sloc)  2.52 KB
 
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

import urllib
import os


#</nfsdb/MODIST/2016/05/08/L2/MODOCT.2016.0508.1436.terra-1.hdf.zip>
#</nfsdb/MODIST/2016/05/09/L2/MODOCBOX.2016.0509.0236.terra-1.hdf.zip>

url1 = 'http://222.236.46.45/nfsdb/'

url2s = ['MODISA/']
#url2s = ['MODIST/']

levels = [#'L1B/',
'L2/' 
#'L3/'
]

filename1s = [ 'MYDOCTaqua-1' ]
# filename1s = ['MODOCTterra-1']


for url2 in url2s :
    for level in levels :
        for filename1 in filename1s :
            save_dir_name = '../{0}{1}/'.format(url2[:-1], level[:-1])
            print(save_dir_name)
            if not os.path.exists(save_dir_name):
                os.makedirs(save_dir_name)
                print ('*'*80)
                print ('{0} is created.'.format(save_dir_name))
            for yr in range(2019, 2020) :
                for mo in range(1, 13) : 
                    for da in range(1, 32) : 
                        for hr in range(0, 24) : 
                            for mi in range(0, 60) : 
                                filename = '{0}.{1:04d}.{2:02d}{3:02d}.{4:02d}{5:02d}.{6}.hdf.zip'.\
                                    format(filename1[:6], yr, mo, da, hr, mi, filename1[6:])
                               

                                if os.path.exists('%s%s' % (save_dir_name, filename)):
                                    print ('*'*40)
                                    print ('{0} is exist'.format(filename))
                    
                                else :
                                                        
                                    try : 
                                        print ('Trying %s' % filename)
                                        url = '{0}{1}{2:04d}/{3:02d}/{4:02d}/{5}{6}'.\
                                            format(url1, url2, yr, mo, da, level, filename)
                                        print(url)
                                    
                                        urllib.request.urlretrieve(url, '{0}{1}'\
                                               .format(save_dir_name, filename))
                                        print('#'*60)
                                        print('{0}{1} is downloaded.'\
                                              .format(save_dir_name, filename))
                                        
                                    except Exception as err : 
                                        print('X'*60)
                                        print('{0}, {1}\n'\
                                              .format(err, url))
                            
