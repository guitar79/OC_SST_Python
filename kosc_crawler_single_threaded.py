import urllib
testfile = urllib.URLopener()
#import httplib
read_file = open('wanted.txt','r')
raw_lists = read_file.read()
urls = []

read_splited = raw_lists.split('<')
#print(read_splited)
for i in range(1,len(read_splited)):
    urls.append("http://222.236.46.45" + read_splited[i].split('>')[0])

#headers = {'User-agent': 'Python'}
#conn = httplib.HTTPConnection('222.236.46.45')

k = 0
while(k < len(urls)):
    try: # This enables us to try downloading again if temporary network error occurs.
        temp = urls[k].split('/')
        filename = urls[k].split('/')[len(temp)-1]
        print ('Downloading ' + filename + '...')
        # conn.request('GET', urls[k], '', headers)
        # resp = conn.getresponse()
        # image = resp.read()
        # f = open('Downloads/' + filename, 'wb')
        # f.write(image)
        testfile.retrieve(urls[k], 'Downloads/' + filename)
        k += 1
    except: # TODO : I can't remember the error name... Can anyone tell me?
        print('Temporary downloading error.')