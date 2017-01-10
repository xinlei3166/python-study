#coding=utf-8

#爬取图片 
import re
import urllib
import urllib2

from lxml import etree

url = "http://www.qiushibaike.com/imgrank/"
headers = { 
	 "User-Agent":	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
}
req = urllib2.Request(url,data=None,headers=headers)
opener = urllib2.urlopen(req)
#print opener
reader = opener.read()
#网页源代码
#print reader

htmlEtree = etree.HTML(reader)
xpaths = htmlEtree.xpath("//img")

for path in xpaths:
	imgPath  = path.attrib['src']
	#print imgPath
	#怎么样拿到图片名
	imgName = imgPath.rsplit("/",1)[1]
	print (imgPath,imgName)
	try:
		urllib.urlretrieve(imgPath,"img/%s"%imgName)
	except:
		pass

	
#scrapy 爬虫框架 做模拟登陆 爬取

