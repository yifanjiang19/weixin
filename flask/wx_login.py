# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urlparse
import urllib2
import re
import requests
import time
import json
import manager
def Download(slave,cookie_ticket,cookie_dataticket):
	url ='https://mp.weixin.qq.com/cgi-bin/newoperatevote?action=show&t=vote/vote_detail&supervoteid=536692316&token=2045985339&lang=zh_CN'
	urls = 'http://mp.weixin.qq.com/s?__biz=MzI5NTQwNzY3Nw==&mid=2247483652&idx=1&sn=39df9f054b6205fd7741ddff2eec6f6d&chksm=ec555856db22d140a745ae9850f0260c44b0e33efe553d5ea54e91b96b0894466381487cd51a&scene=0#wechat_redirect'
	headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
	w = 'https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=529718839'
	q='https://mp.weixin.qq.com/cgi-bin/newoperatevote?action=show&t=vote/vote_detail&supervoteid=443012615&token=358768833&lang=zh_CN'
	cookies = dict(noticeLoginFlag='1',
				remember_acct='331607317%40qq.com',
				tvfe_boss_uuid='6445275c0d5f9431',
				pgv_pvid='7876699616',
				o_cookie='331607317',
				pgv_pvi='8893679616',
				RK='SRfmxaXGEm',
				ptcz='da9d86f6a4737a55eab6ba762a57061e4b82a5eca60a4be0f0cb899c0502df3e',
				pgv_si='s550548480',
				sig='h0107a26704054be52102e3d6da2d5ee5dfdd3b976dc4dbbdf43fa62cf5433ad0d0362c377e42b06b41',
				account='331607317@qq.com',
				cert='gNuMwUAQ03QQOFXiPfEqxSgmqmcGn7RB',
				data_bizuin='3018810863',
				ticket_id='gh_ac1f1cd0d52f',
				ticket= cookie_ticket,
				data_ticket= cookie_dataticket,
				ua_id='cVWE4isNNFIkpbDJAAAAAGi4P8ykwTXaj6HGXgIUGOU=',
				slave_user='gh_ac1f1cd0d52f',
				#slave_sid='SkxiYjRaZllLU21scDZVSVpJM2pja0NDbHpaTF9vZERFTW1Oemd6T21FaXRYYWdqeG1ZVkFBelpuakNvYzVyVEFjQ3EybzV0UXZ3RlNzcnpiSHVQbWx4UnUybGxCVDNOT1I1blV1b3VBb015V3BBTUkxQlBBUzZiZHJkMTRSWUYzTmRISDdhbHU0eTJJSllR',
				#slave_sid = 'VlNrb0xwSFhMcnJEaFB6ZEZFenVPZVlUNlhlQ2h1QVlMN2EwZlZMWmFrZFFwWGY1cXJYOURDTGdDVDJoNHczMGF5a1h1SWZucG84UzdrRHgwWG81ZWplc0x5cE5WdTNtOVY4U1ZkTzRvS2dDUG83RmhIekIzY3B6UHVidWRnYUg5TWdUbG5ZRjNJVDl5ZUFt',
				slave_sid = slave,
				bizuin='3295407677')
	r= requests.get(q,headers=headers,cookies=cookies)
	return r


def spider():
	print("start")
	download = Download('dkN2dGFDVVY4dGZsaDRSSHNleVNQQUNOQzZ1aDhoR0JIbUF2Z0VNUXR1VEd0dXdBYVhOaE5QRDQzMzVXZnVHUU9qY0pBd2NrVThiMVZ1S0Y0aXV6NXdBR184NlpwOVEzNEFQUDhpdm1XakdEREQwcktER2NYUld5bGZENVdZS2VwUE8xellyNW5kWTVubzdL',
						'86f0a4004badd3a47d3b5b0ac452676646811609',
						'KU71up1HwGRucnDyGTPpxFgcoSUYwOqpMe4wX8iWEaH3OQgXy7AGdku8g7bi92az')
	# print(download.text)
	# print download.cookies['slave_sid']
	# fout = open('test.html','w')
	# fout.write("# -*- coding:utf-8 -*-")
	# fout.write(download)
		
	while (1):
		# cookies_slave = download.cookies['slave_sid']
		
		slave = download.cookies['slave_sid']
		print(slave)
		# cookies_ticket = download.cookies['ticket']
		# cookies_dataticket = download.cookies['data_ticket']
		# download = Download(cookies_ticket,cookies_dataticket)
		try:
			download = Download(slave,
						'86f0a4004badd3a47d3b5b0ac452676646811609',
						'KU71up1HwGRucnDyGTPpxFgcoSUYwOqpMe4wX8iWEaH3OQgXy7AGdku8g7bi92az')
		except:
			print("error")
		# print(download.text)
		
		k = re.search(r'wx.cgiData\s=\s{\s.*},\s.*\s.*?}',download.text)
		if k:
			str = k.group(0)
			str = str.replace('wx.cgiData = ','')
			str = str.replace('data','"data"')
			str = str.replace('supervoteid','"supervoteid"')
			print(str)
			a = json.loads(str)
			print(a['data']['vote_subject'][0]['options'][0]['cnt'])
			if not manager.Spider.query.filter_by(name = a['data']['vote_subject'][0]['options'][0]['name']).first():
				asd = manager.Spider(name = a['data']['vote_subject'][0]['options'][0]['name'],
									cnt = a['data']['vote_subject'][0]['options'][0]['cnt'])
		
				manager.db.session.add(asd)
				manager.db.session.commit()
				
			else:
				print("exist")
		else:
			print("not found")	
		
		time.sleep(10)
		pass