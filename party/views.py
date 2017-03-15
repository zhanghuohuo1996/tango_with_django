from django.shortcuts import render
from django.http import HttpResponse,Http404
from django import template
import datetime
from party.models import Partymodel,Jointable
import logging
import MySQLdb
import json
# Create your views here.
def party(request):
	now=datetime.datetime.now()
	fp=open(r'E:\mysite\Gayest\makefriends\templates\party.html')
	t=template.Template(fp.read())
	fp.close()
	db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest",charset="utf8")
	cursor=db.cursor()
	page=request.POST.get('pageNum')
	if(page==None):
		page='1'
		pageint=int(page)
		enchor=12*pageint-12
		num=12
		fp.close()
		cursor.execute("SELECT * FROM gayest.partymodel LIMIT "+str(enchor)+","+str(num))
		result=cursor.fetchall()
		if(request.session['state']==True):
			fp.close()
			logging.debug(result)
			html=t.render(template.Context({'current_date':now,'state':request.session.get('state',default=None),
			'title1':result[0][1],'time1':result[0][2],'address1':result[0][3],
			'title2':result[1][1],'time2':result[1][2],'address2':result[1][3],
			'title3':result[2][1],'time3':result[2][2],'address3':result[2][3],
			'title4':result[3][1],'time4':result[3][2],'address4':result[3][3],
			'title5':result[4][1],'time5':result[4][2],'address5':result[4][3],
			'title6':result[5][1],'time6':result[5][2],'address6':result[5][3],
			'title7':result[6][1],'time7':result[6][2],'address7':result[6][3],
			'title8':result[7][1],'time8':result[7][2],'address8':result[7][3],
			'title9':result[8][1],'time9':result[8][2],'address9':result[8][3],
			'title10':result[9][1],'time10':result[9][2],'address10':result[9][3],
			'title11':result[10][1],'time11':result[10][2],'address11':result[10][3],
			'title12':result[11][1],'time12':result[11][2],'address12':result[11][3],
			'image1':result[0][4],'image2':result[1][4],'image3':result[2][4],
			'image4':result[3][4],'image5':result[4][4],'image6':result[5][4],
			'image7':result[6][4],'image8':result[7][4],'image9':result[8][4],
			'image10':result[9][4],'image11':result[10][4],'image12':result[11][4],
			'username':request.session.get('user_name',default=None)}))
			logging.debug(result[0][4])
			return HttpResponse(html)
		else:
			fp.close()
			html=t.render(template.Context({'current_date':now}))
			return HttpResponse(html)
	else:
		pageint=int(page)
		enchor=12*pageint-12
		num=12
		fp.close()
		cursor.execute("SELECT * FROM gayest.partymodel LIMIT "+str(enchor)+","+str(num))
		result=cursor.fetchall()
		if(request.session['state']==True):
			return HttpResponse(json.dumps(result), content_type="application/json") 
		else:
			fp.close()
			html=t.render(template.Context({'current_date':now}))
			return HttpResponse(html)
def load(request):
    now=datetime.datetime.now()
    fp=open(r'E:\mysite\Gayest\makefriends\templates\party.html')
    t=template.Template(fp.read())
    fp.close()
    db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest",charset="utf8")
    cursor=db.cursor()
    page=request.POST.get('pageNum')
    if(page==None):
		page='1'
		pageint=int(page)
		enchor=12*pageint-12
		num=12
		fp.close()
		cursor.execute("SELECT * FROM gayest.partymodel LIMIT "+str(enchor)+","+str(num))
		result=cursor.fetchall()
		if(request.session['state']==True):
			fp.close()
			logging.debug(result)
			html=t.render(template.Context({'current_date':now,'state':request.session.get('state',default=None),
			'title1':result[0][1],'time1':result[0][2],'address1':result[0][3],
			'title2':result[1][1],'time2':result[1][2],'address2':result[1][3],
			'title3':result[2][1],'time3':result[2][2],'address3':result[2][3],
			'title4':result[3][1],'time4':result[3][2],'address4':result[3][3],
			'title5':result[4][1],'time5':result[4][2],'address5':result[4][3],
			'title6':result[5][1],'time6':result[5][2],'address6':result[5][3],
			'title7':result[6][1],'time7':result[6][2],'address7':result[6][3],
			'title8':result[7][1],'time8':result[7][2],'address8':result[7][3],
			'title9':result[8][1],'time9':result[8][2],'address9':result[8][3],
			'title10':result[9][1],'time10':result[9][2],'address10':result[9][3],
			'title11':result[10][1],'time11':result[10][2],'address11':result[10][3],
			'title12':result[11][1],'time12':result[11][2],'address12':result[11][3],
			'image1':result[0][4],'image2':result[1][4],'image3':result[2][4],
			'image4':result[3][4],'image5':result[4][4],'image6':result[5][4],
			'image7':result[6][4],'image8':result[7][4],'image9':result[8][4],
			'image10':result[9][4],'image11':result[10][4],'image12':result[11][4],
			'username':request.session.get('user_name',default=None)}))
			return HttpResponse(html)
		else:
			fp.close()
			html=t.render(template.Context({'current_date':now}))
			return HttpResponse(html)
    else:
		pageint=int(page)
		enchor=12*pageint-12
		num=12
		fp.close()
		cursor.execute("SELECT * FROM gayest.partymodel LIMIT "+str(enchor)+","+str(num))
		result=cursor.fetchall()                 
		if(request.session['state']==True):
			return HttpResponse(json.dumps(result), content_type="application/json") 
		else:
			fp.close()
			html=t.render(template.Context({'current_date':now}))
			return HttpResponse(html)
def party_detail(request):
	id= request.GET.get('id')
	partyid=int(id)
	now=datetime.datetime.now()
	fp=open(r'E:\mysite\Gayest\makefriends\templates\subparty.html')
	t=template.Template(fp.read())
	fp.close()
	now=datetime.datetime.now()	
	db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest",charset="utf8")
	cursor=db.cursor()
	cursor.execute("SELECT * FROM gayest.partymodel where id = '%d'"%(partyid+1))
	result=cursor.fetchone()
	html=t.render(template.Context({'current_date':now,'state':request.session.get('state',default=None),'result':result,
	'username':request.session.get('user_name',default=None)}))
	return HttpResponse(html)
def ooo(request):
	partyid=request.POST.get('partyid')
	username=request.POST.get('username')
	result={}
	result['message']='already join'
	db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest",charset="utf8")
	cursor=db.cursor()
	cursor.execute("SELECT * FROM gayest.jointable where partyid = '%d'and username='%s'"%(int(partyid),username))
	count=cursor.fetchone()
	logging.debug("hhhhhhhhhhhhhhhhhhhhh")
	if(count!=None):
		return HttpResponse(json.dumps(result),content_type="application/json")
	else:
		cursor.execute("INSERT INTO gayest.jointable(partyid,username) VALUES('%d','%s')"%(int(partyid),username))
		db.commit()
		result['message']='join success'
		return HttpResponse(json.dumps(result),content_type="application/json")