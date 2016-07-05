import shutil
import os


def mvimg():
    with open('tmp.log' ,'r', encoding='UTF-8') as f:
        for n in f.readlines():
            a = n.split('/')
            print(a)
            print(a[5])
            print(a[6].strip())
            src_path = os.path.join('/'"/tmp","img",a[5],a[6].strip())
            dst_path = os.path.join('/mnt','data','cms','uploads','allimg',a[5],a[6].strip())
            print(src_path)
            print(dst_path)

# !/usr/bin/python
import os
url_list = []
geturl_list = []
# rootdir = "/mnt/data/cms/a/meinv/2016/0703"
rootdir = "C:\\Users\\zhangjun\\PycharmProjects\\s12\\cms.jjos\\html\\"
os.chdir(rootdir)
for dirpath, dirnames, filenames  in os.walk(rootdir):
    # print('dirpath:',dirpath)
    # print('dirnames:',dirnames)
    # print('filenames',filenames)
    for html in filenames:
        # file_path = os.path.join(dirpath,file)
        with open(html,'r',encoding='UTF-8',) as f:
            for i in f.readlines():
                if  i.__contains__("<img src='http"):
                    l = i.strip()
                    url = l.split(sep="'")
                    geturl_list.append(url[1])
# print(geturl_list)


import urllib
# import urllib2
import requests

def download():
    for url in geturl_list:
        print("downloading with urllib")
        # urllib.urlretrieve(url, "demo.zip")
        request = requests.get(url)
        # response = reques
        # print(response.read())

download()
                    # url_list.append(i.strip())










