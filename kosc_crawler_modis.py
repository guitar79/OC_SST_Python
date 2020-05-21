import urllib.request as urllib
import os

#</nfsdb/MODIST/2016/05/08/L2/MODOCT.2016.0508.1436.terra-1.hdf.zip>
#</nfsdb/MODIST/2016/05/09/L2/MODOCBOX.2016.0509.0236.terra-1.hdf.zip>

base_url = 'http://222.236.46.45/nfsdb/'

moids_data_els = [('MODISA/', 'L2/', 'MYDOCT', 'aqua-1'),
                  ('MODISA/', 'L2/', 'MYDOCSST', 'aqua-1'), # after 2019
                  ('MODIST/', 'L2/', 'MODOCT', 'terra-1'),
                ('MODIST/', 'L2/', 'MODOCSST', 'terra-1'), # after 2019
                ('MODISA/', 'L2/', 'MODOCX', 'aqua-1'),
                ('MODIST/', 'L2/', 'MODOCX', 'terra-1')
                ]

for yr in range(2011, 2020) :
    for mo in range(1, 13) : 
        for da in range(1, 32) : 
            for hr in range(0, 24) : 
                for mi in range(0, 60) : 
                    for moids_data_el in moids_data_els :
                        save_dir_name = '../{0}{1}/'.format(moids_data_el[0][:-1], moids_data_el[1][:-1])
                        print(save_dir_name)
                        if not os.path.exists(save_dir_name):
                            os.makedirs(save_dir_name)
                            print ('*'*80)
                            print ('{0} is created.'.format(save_dir_name))
                            
                        filename = '{0}.{1:04d}.{2:02d}{3:02d}.{4:02d}{5:02d}.{6}.hdf.zip'.\
                            format(moids_data_el[2], yr, mo, da, hr, mi, moids_data_el[3])
                       
                        if os.path.exists('%s%s' % (save_dir_name, filename)):
                            print ('*'*40)
                            print ('{0} is exist'.format(filename))
            
                        else :
                                                
                            try : 
                                print ('Trying %s' % filename)
                                url = '{0}{1}{2:04d}/{3:02d}/{4:02d}/{5}{6}'.\
                                    format(base_url, moids_data_el[0], yr, mo, da, moids_data_el[1], filename)
                                print(url)
                            
                                urllib.urlretrieve(url, '{0}{1}'\
                                       .format(save_dir_name, filename))
                                print('#'*60)
                                print('{0}{1} is downloaded.'\
                                      .format(save_dir_name, filename))
                                
                            except Exception as err : 
                                print('X'*60)
                                print('{0}, {1}\n'\
                                      .format(err, url))
                    