import urllib.request
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    #serviceurl = 'http://python-data.dr-chuck.net/comments_42.xml'
    serviceurl = 'http://python-data.dr-chuck.net/comments_221445.xml'
    url=input('Enter location :')
    if len(url)<1:
        url=serviceurl
    print('Retrieving: ' + url)
    uh=urllib.request.urlopen(url )
    data=uh.read()
    print('Retrived ' + str(len(data)) + ' characters')
    tr=ET.fromstring(data)
    cnt=tr.findall('.//count')
    s=0

# this is ubuntu version

    
    # this is windows work version
    for c in cnt:
        s+=int(c.text)
    print ('Count:' + str(len(cnt)))
    print ('Sum:' + str(s))