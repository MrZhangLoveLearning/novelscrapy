# coding=utf-8
"""The database helper"""
from sqlalchemy import func, or_, not_
import connection
import model
import logging
import send_email
Article=model.Article
def is_exist_url(url):
	session=connection.init_db()
	query=session.query(Article)
	aritcle=query.filter(Article.art_url==url).scalar()
	if aritcle:
		return 1
	return 0
def save_art(art_url, art_type, art_title, content):
	art={}
	# send_mail(mailto_list,"hello",content)
	art['art_url']=art_url
	art['art_type']=art_type
	art['art_title']=art_title
	art['content']=content
	art['is_send']=False
	artic=Article(**art)
	session=connection.init_db()
	session.add(artic)
	session.commit()
def count():
	session=connection.init_db()
	query=session.query(Article)
	count=session.query(func.count('*')).filter(Article.is_send==False).scalar()
	return count

title=u"<div><a href=\"%s\">%s</a></div>"
message=u'today have no news'

def get_send_content(num, to_self=False):
	content = []
	session = connection.init_db()
	query = session.query(Article)
	get_all = num
	get_url = None
	total_count = count()
	print 'send the email count:%d'%total_count
	if total_count == 0:
		return message
	if total_count > num :
		get_url = total_count-num
	else:
		get_all = total_count
	if to_self:
		get_all = total_count
		get_url = None
	for a in query.filter(Article.is_send == False).order_by(Article.id.desc()).limit(get_all).all():
		box = []
		box.append(title%(a.art_url, a.art_title))
		box.append(a.content)
		content.append(u''.join(box))
	if get_url:
		for a in query.filter(Article.is_send == False).order_by(Article.id.desc()).offset(num).limit(get_url).all():
			box = []
			box.append(title%(a.art_url, a.art_title))
			content.append(u''.join(box))
	send_content = u''.join(content)
	return send_content



def get_courrent_time():
	import time
	ISOTIMEFORMAT='%Y-%m-%d'
	return time.strftime( ISOTIMEFORMAT, time.localtime())	
def clear_email(is_clean=1):
	session=connection.init_db()
	session.execute('update article set is_send=%d'%is_clean)
	session.commit()
	for i in session.query(Article).all():
		if i.is_send:
			print i.art_url+' \t'+'had send'
		else:
			print i.art_url+'\t'+'do not send'
	
def send_art_email(to_self=False):
	content=get_send_content(10,to_self)
	if to_self:
		clear_email()
	print content
	return send_email.send_mail('novels newest',content,to_self)

# clear_email(0)
# save_art('d','d','test')

# is_exist_url('df') 
# connection.drop_db()
#7
#13
#14
#38
#95
# print count()
# # print count()
# clear_email()