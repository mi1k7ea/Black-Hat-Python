#!/usr/bin/python
#coding=utf-8
import urllib2

url = "http://www.baidu.com"

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close()
# body = urllib2.urlopen("http://www.baidu.com")

# print body.read()