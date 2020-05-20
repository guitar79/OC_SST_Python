import urllib
import os


#</nfsdb/MODIST/2016/05/08/L2/MODOCT.2016.0508.1436.terra-1.hdf.zip>
#</nfsdb/MODIST/2016/05/09/L2/MODOCBOX.2016.0509.0236.terra-1.hdf.zip>

url1 = 'http://222.236.46.45/nfsdb/'

url2s = [
'MODISA/'
]
url2s = [
'MODIST/'
]

levels = [
#'L1B/',
'L2/'
#'L3/',
]

filename1s = [
'MYDOCAaqua-1'
]
filename1s = [
'MODOCTterra-1'
]



for url2 in url2s :
    for level in levels :
        for filename1 in filename1s :
            save_dir_name = '../{0}{1}/'.format(url2[:-1], level[:-1])
            print(save_dir_name)
            if not os.path.exists(save_dir_name):
                os.makedirs(save_dir_name)
                print ('*'*80)
                print ('{0} is created.'.format(save_dir_name))
            for yr in range(2017, 2019) :
                for mo in range(1, 13) : 
                    for da in range(1, 32) : 
                        for hr in range(0, 24) : 
                            for mi in range(0, 60) : 
                                filename = '{0}.{1:04d}.{2:02d}{3:02d}.{4:02d}{5:02d}.{6}.hdf.zip'.\
                                    format(filename1[:6], yr, mo, da, hr, mi, filename1[6:])
                               

                                if os.path.exists('%s/%s' % (save_dir_name, filename)):
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
                            