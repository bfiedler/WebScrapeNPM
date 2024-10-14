# downloads stamp images from National Postal Museum
import os, sys
from urllib.error import HTTPError
import urllib.request



def status(url):
    try:
        response = urllib.request.urlopen(url)
        response_status = response.status  # 200, 301, etc
    except HTTPError as error:
        response_status = error.code  # 404, 500, etc`
    return response_status


head = "https://ids.si.edu/ids/deliveryService?id="
npm = "NPM-1980_2493_{:04d}"

# use range(2200, 6100) to get several hundred images
for n in range(5000, 5010):  # this range for a sample of images
    u = npm.format(n)
    url = head + u
    st = status(url)
    print(url, st)
    ouf = u + '.jpg'
    if st == 200 and not os.path.exists(ouf):
        urllib.request.urlretrieve(url, ouf)
        filesize = os.path.getsize(ouf)
        print(filesize)
