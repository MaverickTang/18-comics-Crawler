import re
from urllib.request import urlretrieve
import urllib

IMAGE_URL = "https://cdn-msp.18comic.vip/media/photos/85637/00001.jpg"
#urlretrieve方法
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
urlretrieve(IMAGE_URL, '/Users/maverick/Desktop/test/1.jpg')
#urlretrieve('https://cdn-msp.18comic.vip/media/photos/119342/00001.jpg', '/Users/maverick/Desktop/test/1.jpg')





#preimgfront = ['https://18comic.vip/album/147835/omo-%E9%AC%BC%E7%95%9C%E7%8E%8B%E6%B1%89%E5%8C%96%E7%BB%84-c97-%E3%81%97%E3%81%BE%E3%81%B1%E3%82%93-%E7%AB%8B%E8%8A%B1%E3%82%AA%E3%83%9F%E3%83%8A-%E7%95%B0%E4%B8%96%E7%95%8C%E3%83%8F%E3%83%BC%E3%83%AC%E3%83%A0%E7%89%A9%E8%AA%9E%E5%A4%96%E4%BC%9D-%E3%83%8A%E3%82%BF%E3%83%AA%E3%83%A4%E7%B7%A8-%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB-%E7%84%A1%E4%BF%AE%E6%AD%A3']
#base='https://18comic.vip'
##for i in range(len(link_urls)):
#	matchObj = re.search( r'album', link_urls[i], re.M|re.I)
#	if matchObj:
#		h=base+link_urls[i]
#		print("",h)
#	else:
#		print("Failed")
#print(len(link_urls))
#pfront=preimgfront[0].split('/')
#a=''
#for i in range(len(pfront)-1):	# 循环输出列表值
#	h=pfront[i]+'/'
#	a=a+h
#print(a)
#link_urls=[]
#url='https://18comic.vip/album/147835/omo-%E9%AC%BC%E7%95%9C%E7%8E%8B%E6%B1%89%E5%8C%96%E7%BB%84-c97-%E3%81%97%E3%81%BE%E3%81%B1%E3%82%93-%E7%AB%8B%E8%8A%B1%E3%82%AA%E3%83%9F%E3%83%8A-%E7%95%B0%E4%B8%96%E7%95%8C%E3%83%8F%E3%83%BC%E3%83%AC%E3%83%A0%E7%89%A9%E8%AA%9E%E5%A4%96%E4%BC%9D-%E3%83%8A%E3%82%BF%E3%83%AA%E3%83%A4%E7%B7%A8-%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB-%E7%84%A1%E4%BF%AE%E6%AD%A3'
#preurl=url.split('/')
#url=''
#for i in range(len(preurl)-1):
#	if preurl[i]=='album':
#		h='photo/'
#	else:
#		h=preurl[i]+'/'
#	url=url+h
#link_urls.append(url)
#print("",link_urls[0])
#print(str(10))