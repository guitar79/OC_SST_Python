import urllib.request as urllib
import time
#threading library
import threading
import sys
import os


prefix = 'AWS-01min'

#single thread class
class crawler():
    def __init__(self, year, month, day, hour, minute, threadno) :
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.threadno = threadno
        
    def fetch(self, moids_data_el):
        base_url = 'http://222.236.46.45/nfsdb/'
        save_dir_name = '../{0}_{1}_{2}/'.format(moids_data_el[1][:-1], moids_data_el[4], moids_data_el[5])
        print(save_dir_name)
        if not os.path.exists(save_dir_name):
            os.makedirs(save_dir_name)
            print ('*'*80)
            print ('{0} is created.'.format(save_dir_name))
		
        if moids_data_el[5] == 'NOAA' :
            filename = '{0}{1:04d}.{2:02d}{3:02d}.{4:02d}{5:02d}.{6}'\
                    .format(moids_data_el[2], self.year, self.month, self.day, self.hour, self.minute, moids_data_el[3])
        else :                     
            filename = '{0}.{1:04d}.{2:02d}{3:02d}.{4:02d}{5:02d}.{6}'\
                .format(moids_data_el[2], self.year, self.month, self.day, self.hour, self.minute, moids_data_el[3])
        
        url = '{0}{1}{2:04d}/{3:02d}/{4:02d}/{5}{6}'.\
                    format(base_url, moids_data_el[0], 
                           self.year, self.month, self.day, 
                           moids_data_el[1], filename)
        print(url)
        print ('Trying {0}'.format(filename))
            
        if os.path.exists('%s%s'.format(save_dir_name, filename)):
            print ('*'*40)
            print ('{0} is exist'.format(filename))
            #time.sleep(1)
        
        else:	
            
            try : 
                urllib.urlretrieve(url, '{0}{1}'\
                       .format(save_dir_name, filename))
                print('#'*60)
                print('#'*60)
                print('#'*60)
                print('#'*60)
                print('#'*60)
                print('{0}{1} is downloaded.'\
                      .format(save_dir_name, filename))
                #time.sleep(1)
                            
            except Exception as err : 
                print('X'*60)
                sys.stderr.write("Thread #{0:d} failed...\n{1}, {2}\n".format(self.threadno, err, url))
                pass
                  
#crawler for single day
class crawler_month(threading.Thread):
    def __init__(self, year, month, threadno, moids_data_el):
        threading.Thread.__init__(self)
        self.year = year
        self.month = month
        self.threadno = threadno
        sys.stderr.write('Thread #{0:d} started...\n'.format(self.threadno))

    def run(self):
        for Da in range(1, 32):
            for Ho in range(0, 24):
                for Mn in range(0, 60):                 
                    fetcher = crawler(self.year, self.month, Da, Ho, Mn, self.threadno)
                    fetcher.fetch(moids_data_el)
                    sys.stderr.write('Thread #{0:d} - fetched {1:d}-{2:02d}-{3:02d} {4:02d}:{5:02d}...\n'\
                         .format(self.threadno, self.year, self.month, Da, Ho, Mn))
                        
#</nfsdb/MODIST/2016/05/08/L2/MODOCT.2016.0508.1436.terra-1.hdf.zip>
#</nfsdb/MODIST/2016/05/09/L2/MODOCBOX.2016.0509.0236.terra-1.hdf.zip>
#</nfsdb/NOAA/2013/12/22/L2/2013.1222.0659.noaa-18.sst.asc.zip>

threadno = 0
moids_data_els = [('MODISA/', 'L2/', 'MYDOCT', 'aqua-1.hdf.zip', 'SST', 'MODIS'),                  
                  ('MODIST/', 'L2/', 'MODOCT', 'terra-1.hdf.zip', 'SST', 'MODIS'),
                  ('MODISA/', 'L2/', 'MYDOCX', 'aqua-1.hdf.zip', 'CHL', 'MODIS'),
                  ('MODIST/', 'L2/', 'MODOCX', 'terra-1.hdf.zip', 'CHL', 'MODIS'),
                  ('MODISA/', 'L2/', 'MYDOCBOX', 'aqua-1.hdf.zip', 'CHL', 'MODIS'),
                  ('MODIST/', 'L2/', 'MODOCBOX', 'terra-1.hdf.zip', 'CHL', 'MODIS'),
                  ('MODISA/', 'L2/', 'MYDOCSST', 'aqua-1.hdf.zip', 'SST', 'MODIS'), # after 2019
                  ('MODIST/', 'L2/', 'MODOCSST', 'terra-1.hdf.zip', 'SST', 'MODIS'),# after 2019
                  ('NOAA/', 'L2/', '', 'noaa-16.sst.asc.zip', 'SST', 'NOAA'),
                  ('NOAA/', 'L2/', '', 'noaa-17.sst.asc.zip', 'SST', 'NOAA'),
                  ('NOAA/', 'L2/', '', 'noaa-18.sst.asc.zip', 'SST', 'NOAA'),
                  ('NOAA/', 'L2/', '', 'noaa-19.sst.asc.zip', 'SST', 'NOAA')]

for Yr in range(2011,2020):
    for Mo in range(1,13):
        for moids_data_el in moids_data_els:
            cmonth = crawler_month(Yr, Mo, threadno, moids_data_el)
            cmonth.start()
            threadno += 1
