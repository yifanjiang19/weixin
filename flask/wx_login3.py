# -*- coding:utf-8 -*-

import re
import requests
import time
import json
import manager
def Download():
	url ='https://mp.weixin.qq.com/cgi-bin/newoperatevote?action=show&t=vote/vote_detail&supervoteid=536692316&token=2045985339&lang=zh_CN'
	urls = 'http://mp.weixin.qq.com/s?__biz=MzI5NTQwNzY3Nw==&mid=2247483652&idx=1&sn=39df9f054b6205fd7741ddff2eec6f6d&chksm=ec555856db22d140a745ae9850f0260c44b0e33efe553d5ea54e91b96b0894466381487cd51a&scene=0#wechat_redirect'
	headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
	w = 'https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=529718839'
	project_url='https://mp.weixin.qq.com/cgi-bin/newoperatevote?action=show&t=vote/vote_detail&supervoteid=443096870&token=1112915088&lang=zh_CN'
	group_url = 'https://mp.weixin.qq.com/cgi-bin/newoperatevote?action=show&t=vote/vote_detail&supervoteid=443038292&token=1112915088&lang=zh_CN'
	cookies = dict(
				# annual_review_dialog = '1',
				# noticeLoginFlag='1',
				# remember_acct='892445964%40qq.com',
				
				# pgv_pvid='7876699616',
				
				# pgv_pvi='1393451008',
			
				# pgv_si='s9889421312',#change
				# account='892445964@qq.com',
				# cert='b4Uqap0NTS04oeM0n7uT_TiOorGLJ5DP',#change
				# data_bizuin='3000802809',
				# ticket_id='gh_d2278a1b9c37',
				# ticket= cookie_ticket,
				# data_ticket= cookie_dataticket,
				# ua_id='7rXZjH2TbdjDlRSnAAAAAKWCvDbAIxa1UvcEXZ3DbxM=',
				# slave_user='gh_d2278a1b9c37',
				# slave_sid = slave,
				# bizuin='3087896448',
				# annual_review_dialog='1',
				pgv_pvi='1393451008',
 				pgv_si='s9889421312',
				account='892445964@qq.com',
				cert='b4Uqap0NTS04oeM0n7uT_TiOorGLJ5DP', 
				data_bizuin='3000802809',
				ticket_id='gh_d2278a1b9c37',
				ticket='1f71c9c4a0ca22cd3632344bff9196dea2ca3759; data_ticket=q+dEwCWO3Y7f0DJn9h2U1sKPMaFg+naHRosLn0kEQgxJRQstM99jRzLDDojl/WHa', 
				data_ticket='q+dEwCWO3Y7f0DJn9h2U1sKPMaFg+naHRosLn0kEQgxJRQstM99jRzLDDojl/WHa',
				noticeLoginFlag='1',
				remember_acct='892445964%40qq.com',
				ua_id='7rXZjH2TbdjDlRSnAAAAAKWCvDbAIxa1UvcEXZ3DbxM=', 
				slave_user='gh_d2278a1b9c37',
				slave_sid='TmJQeGVyN0dEN1JZRDUwU2tVRU85T3pPSmxVV05PVFBxN1FUdFZQOEtaTVBkY3pZSGx1cjZLOUJndWtXOTF6Wkw4OU16Sm1LWUlFalZQanY0VkhTTDNtalA2YkRHYzdISFpWVU9VMDBKYkdvYWc2QW1FS0pqNXJoOVNNSmdObkFPQXQyZHA0aUF5ck5xYmFP',
				bizuin='3087896448')
	r= requests.get(group_url,headers=headers,cookies=cookies)
	return r


def spider():
	print("start")
	download = Download()

	while (1):
		try:
			slave = download.cookies['slave_sid']
			print(download.cookies.keys())	
		except:
			print("cookies error!")

		download = Download()
		print("error")
		print(download.text)
		k = re.search(r'wx.cgiData\s=\s{\s.*},\s.*\s.*?}',download.text)
		print(k)
		if k:
			str = k.group(0)
			str = str.replace('wx.cgiData = ','')
			str = str.replace('data','"data"')
			str = str.replace('supervoteid','"supervoteid"')
			print(str)
			a = json.loads(str)
			# print a
			for i in range(18):	
				if not manager.Group.query.filter_by(name = a['data']['vote_subject'][0]['options'][i]['name']).first():
					asd = manager.Group(name = a['data']['vote_subject'][0]['options'][i]['name'],
										cnt = a['data']['vote_subject'][0]['options'][i]['cnt'],
										num = i)	
					manager.db.session.add(asd)
					manager.db.session.commit()
			
				else:
					asd = manager.Group.query.filter_by(name = a['data']['vote_subject'][0]['options'][i]['name']).first()			
					asd.name = a['data']['vote_subject'][0]['options'][i]['name']
					asd.cnt = a['data']['vote_subject'][0]['options'][i]['cnt']
					asd.num = i
					manager.db.session.add(asd)
					manager.db.session.commit()

		else:
			print("not found")	

		time.sleep(10)
		pass