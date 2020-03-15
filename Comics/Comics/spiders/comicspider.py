# -*- coding: utf-8 -*-
import scrapy
import re
import os
import urllib
import zlib
import time
from urllib.request import urlretrieve
import urllib

class ComicSpider(scrapy.Spider):
	name = "comic"
	start_urls = ['https://18comic.vip/photo/1935/']
	allowed_domains = ['https://18comic.vip','https://cdn-msp.18comic.vip/']

	def parse(self, response):
		preimg=response.xpath('//div[contains(@id,".jpg")]/@id').extract()
		preimgfront=response.xpath('//img[contains(@src,"https://cdn-msp.18comic.vip/")]/@src').extract()
		ptitle=response.xpath('//title/text()').extract()
		title=ptitle[0]
		pfront=preimgfront[0].split('/')
		base=''
		img_urls=[]
		for i in range(len(pfront)-1):	# 循环输出列表值
			h=pfront[i]+'/'
			base=base+h
		for i in range(len(preimg)):
			urlm=base+preimg[i]
			img_urls.append(urlm)
#			print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#			print("",img_urls[i])
		document = '/Users/maverick/Documents/骚操作的文件夹/漫画下载'
		comics_path = document + '/' + title
		exists = os.path.exists(comics_path)
		if not exists:
#				self.log('create document: ' + title)
			os.makedirs(comics_path)
			for i in range(len(img_urls)):
				print(">>>>>>>>>>>>>>>>Downloading<<<<<<<<<<<<<<<<<:")
				print(img_urls[i])
				pic_name = comics_path + '/' +str(i)+ '.jpg'
				print(pic_name)
				exists = os.path.exists(pic_name)
				if not exists:
					time.sleep(0.1)#防止锁ip
					opener=urllib.request.build_opener()#骚操作克制反爬虫服务器
					opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
					urllib.request.install_opener(opener)
					urlretrieve(img_urls[i], pic_name)
				else:
					self.log('图片已下载')
		else:
			self.log('漫画已下载')	
				
		