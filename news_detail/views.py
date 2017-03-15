from django.shortcuts import render
from django.http import HttpResponse,Http404
from django import template
import datetime
import os
from news_detail.models import Newsmodel
from news.models import NewsComment
from django.http import HttpResponseRedirect
#from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import logging
import string
# Create your views here.
def news_detail(request):
	#name = request.REQUEST.get('name','xxx')
	id= request.GET.get('id')
	now=datetime.datetime.now()	
	db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest",charset="utf8")
	cursor=db.cursor()
	cursor.execute("SELECT * FROM gayest.newsmodel where id = '%d'"%(0))
	result=cursor.fetchone()
	cursor.execute("SELECT * FROM gayest.news_comment where newsid = '%d'"%(0))
	comment=cursor.fetchall()
	num=1
	if(id=='0'):
		cursor.execute("SELECT * FROM gayest.newsmodel where id = '%d'"%(0))
		result=cursor.fetchone()
		cursor.execute("SELECT * FROM gayest.news_comment where newsid = '%d'"%(0))
		comment=cursor.fetchall()
		num=len(comment)
	if(id=='1'):
		cursor.execute("SELECT * FROM gayest.newsmodel where id = '%d'"%(1))
		result=cursor.fetchone()
		cursor.execute("SELECT * FROM gayest.news_comment where newsid = '%d'"%(1))
		comment=cursor.fetchall()
		num=len(comment)
	if(id=='2'):
		cursor.execute("SELECT * FROM gayest.newsmodel where id = '%d'"%(2))
		result=cursor.fetchone()
		cursor.execute("SELECT * FROM gayest.news_comment where newsid = '%d'"%(2))
		comment=cursor.fetchall()
		num=len(comment)
	fp=open(r'E:\mysite\Gayest\makefriends\templates\single.html')
	t=template.Template(fp.read())
	#news_article=Newsmodel.objects.all()
	#path = news_article[1].filepath.replace("//","\")
	#all_the_text=news_article[0].filepath
	html = t.render(template.Context({'current_date':now,'file':result[1],'title':result[2],'newsimage':result[3],'num':num,'comment':comment}))
	logging.debug(comment)
	logging.debug(num)
	return HttpResponse(html)
def comment(request):
	now=datetime.date.today()
	newsid=request.POST.get('newsid','')
	id=string.atoi(newsid)
	name=request.POST.get('name','')
	comment=request.POST.get('comment','')
	db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest")
	db.set_character_set('utf8')  
	cursor=db.cursor()
	logging.debug(newsid)
	logging.debug(id)
	sql='INSERT INTO news_comment(newsid,name,comment,date)values("%d","%s","%s","%s")'%(id,name,comment,now)
	cursor.execute(sql)
	db.commit()
	db.close()
	return HttpResponseRedirect("http://127.0.0.1:8001/single.html?id="+newsid)