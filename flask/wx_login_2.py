# -*- coding:utf-8 -*-



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
	project_url='https://mp.weixin.qq.com/cgi-bin/newoperatevote?action=show&t=vote/vote_detail&supervoteid=443096870&token=1112915088&lang=zh_CN'
	group_url = 'https://mp.weixin.qq.com/cgi-bin/newoperatevote?action=show&t=vote/vote_detail&supervoteid=443038292&token=688196857&lang=zh_CN'
	cookies = dict(pgv_pvi='1393451008',
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
	r= requests.get(project_url,headers=headers,cookies=cookies)
	return r


def spider():
	print("start")
	download = Download('ZVZrM2dYaENLSUNPMHNxaWpXWHR6NGRoU2pVMnE3Y0lRdnJJX0NOX2pUMkF5Z1lpRDd2b2lmZ2dVaWNTNXVuREN3SXo1dV9idFMwaDhUSHIxbGxkUnU5V3ZpazVTZ1R1STFEeWR3bE1RN2p4Mk1VcXN4U2FtQlM2WkFFNkNXaHRLbnFRN0VRMVhrS0EzdjYy',
						'4f81582140b76fbbcb1d3b9b4b85e9f30bef2571',
						'U7zh/ac5QIGsq/SJSZYBvZ1fXRQQrvqM05uU39Awl/PyHXokhLlIwPQ/HQHiPExK')
	# print(download.text)
	# print download.cookies['slave_sid']
	# fout = open('test.html','w')
	# fout.write("# -*- coding:utf-8 -*-")
	# fout.write(download)
		
	while (1):
		# cookies_slave = download.cookies['slave_sid']
		# print(download.text)
		try:
			slave = download.cookies['slave_sid']
			print(download.cookies.keys())	
		except:
			print("cookies error!")
			
		# cookies_ticket = download.cookies['ticket']
		# cookies_dataticket = download.cookies['data_ticket']
		# download = Download(cookies_ticket,cookies_dataticket)
		try:
			download = Download(slave,
						'4f81582140b76fbbcb1d3b9b4b85e9f30bef2571',
						'U7zh/ac5QIGsq/SJSZYBvZ1fXRQQrvqM05uU39Awl/PyHXokhLlIwPQ/HQHiPExK')
		except:
			print("error")
		# print(download.text)
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
			# print(a['data']['vote_subject'][0]['options'][0]['cnt'])
			for x in range(3):
				for i in range(30):	
					num = x*30+i+1
					# print(num)
					# print(a['data']['vote_subject'][x]['options'][i]['name'])
					if not manager.Spider.query.filter_by(name = a['data']['vote_subject'][x]['options'][i]['name']).first():
						asd = manager.Spider(name = a['data']['vote_subject'][x]['options'][i]['name'],
											cnt = a['data']['vote_subject'][x]['options'][i]['cnt'],
											num = num)
		
						manager.db.session.add(asd)
						manager.db.session.commit()

				
					else:
						asd = manager.Spider.query.filter_by(name = a['data']['vote_subject'][x]['options'][i]['name']).first()
						asd.name = a['data']['vote_subject'][x]['options'][i]['name']
						asd.cnt = a['data']['vote_subject'][x]['options'][i]['cnt']
						asd.num = num
						manager.db.session.add(asd)
						manager.db.session.commit()
						# manager.db.session.delete(dele)
						# asd = manager.Spider(name = a['data']['vote_subject'][x]['options'][i]['name'],
											# cnt = a['data']['vote_subject'][x]['options'][i]['cnt'])
						# manager.db.session.add(asd)
						# manager.db.session.commit()
			for i in range(20):	
					num = 90+ i +1
					# print(num)
					# print(a['data']['vote_subject'][3]['options'][i]['name'])
					if not manager.Spider.query.filter_by(name = a['data']['vote_subject'][3]['options'][i]['name']).first():
						asd = manager.Spider(name = a['data']['vote_subject'][3]['options'][i]['name'],
											cnt = a['data']['vote_subject'][3]['options'][i]['cnt'],
											num = num)
		
						manager.db.session.add(asd)
						manager.db.session.commit()
				
					else:
						asd = manager.Spider.query.filter_by(name = a['data']['vote_subject'][3]['options'][i]['name']).first()
						asd.name = a['data']['vote_subject'][3]['options'][i]['name']
						asd.cnt = a['data']['vote_subject'][3]['options'][i]['cnt']
						asd.num = num
						manager.db.session.add(asd)
						manager.db.session.commit()

		else:
			print("not found")	

		time.sleep(10)
		pass