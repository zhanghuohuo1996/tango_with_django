#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django import template
from django.http import HttpResponseRedirect
import datetime
import logging
import MySQLdb
import string 
import json
from makefriends.models import Datingmodel
from makefriends.models import Liketable

db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest",charset="utf8")
cursor=db.cursor()

# Create your views here.
def hello(request):
	now=datetime.datetime.now()
	fp=open(r'E:\mysite\Gayest\makefriends\templates\dating.html')
	t=template.Template(fp.read())
	
	page=request.GET.get('p')
	
	if(page==None):
		page='1'
		return HttpResponseRedirect('http://127.0.0.1:8001/dating.html?p=1')
	pageint=int(page)
	enchor=24*pageint-24
	num=24
	num_list=[]
	temp=[]
	temp_list=[]
	temp1=[]
	inf=0
	fp.close()
	cursor.execute("SELECT * FROM gayest.datingmodel LIMIT "+str(enchor)+","+str(num))
	result=cursor.fetchall()
	#logging.debug(result[1][1])
	if(request.session['state']==True):
		cursor.execute("SELECT * FROM gayest.liketable where username = '%s'"%(request.session.get('user_name',default=None)))
		like_list=cursor.fetchall()
		for i in range(0,24):
			cursor.execute("SELECT * FROM gayest.liketable where likename = '%s'"%result[i][1])
			cursor.fetchall()
			a=str(cursor.rowcount)
			num_list.append(a)
		# i in range(4):
			#temp_list.append(num_list.index(max(num_list)))
		temp=num_list
		temp.sort()	
		logging.debug(temp)
		temp_list.append(num_list.index(temp[23]))
		temp_list.append(num_list.index(temp[22]))
		temp_list.append(num_list.index(temp[21]))
		temp_list.append(num_list.index(temp[20]))
		#for j in range(0,4):
			#if(temp!=None):
				#temp_list.append(num_list.index(temp.pop()))
		#num_list=["11","12","13"]
		#logging.debug(temp_list)
		#if(len(temp_list)==4):
		html=t.render(template.Context({'current_date':now,'state':request.session.get('state',default=None),
		'name1':result[0][1],'sex1':result[0][2],'age1':result[0][3],'address1':result[0][4],
		'name2':result[1][1],'sex2':result[1][2],'age2':result[1][3],'address2':result[1][4],
		'name3':result[2][1],'sex3':result[2][2],'age3':result[2][3],'address3':result[2][4],
		'name4':result[3][1],'sex4':result[3][2],'age4':result[3][3],'address4':result[3][4],
		'name5':result[4][1],'sex5':result[4][2],'age5':result[4][3],'address5':result[4][4],
		'name6':result[5][1],'sex6':result[5][2],'age6':result[5][3],'address6':result[5][4],
		'name7':result[6][1],'sex7':result[6][2],'age7':result[6][3],'address7':result[6][4],
		'name8':result[7][1],'sex8':result[7][2],'age8':result[7][3],'address8':result[7][4],
		'name9':result[8][1],'sex9':result[8][2],'age9':result[8][3],'address9':result[8][4],
		'name10':result[9][1],'sex10':result[9][2],'age10':result[9][3],'address10':result[9][4],
		'name11':result[10][1],'sex11':result[10][2],'age11':result[10][3],'address11':result[10][4],
		'name12':result[11][1],'sex12':result[11][2],'age12':result[11][3],'address12':result[11][4],
		'name13':result[12][1],'sex13':result[12][2],'age13':result[12][3],'address13':result[12][4],
		'name14':result[13][1],'sex14':result[13][2],'age14':result[13][3],'address14':result[13][4],
		'name15':result[14][1],'sex15':result[14][2],'age15':result[14][3],'address15':result[14][4],
		'name16':result[15][1],'sex16':result[15][2],'age16':result[15][3],'address16':result[15][4],
		'name17':result[16][1],'sex17':result[16][2],'age17':result[16][3],'address17':result[16][4],
		'name18':result[17][1],'sex18':result[17][2],'age18':result[17][3],'address18':result[17][4],
		'name19':result[18][1],'sex19':result[18][2],'age19':result[18][3],'address19':result[18][4],
		'name20':result[19][1],'sex20':result[19][2],'age20':result[19][3],'address20':result[19][4],
		'name21':result[20][1],'sex21':result[20][2],'age21':result[20][3],'address21':result[20][4],
		'name22':result[21][1],'sex22':result[21][2],'age22':result[21][3],'address22':result[21][4],
		'name23':result[22][1],'sex23':result[22][2],'age23':result[22][3],'address23':result[22][4],
		'name24':result[23][1],'sex24':result[23][2],'age24':result[23][3],'address24':result[23][4],
		'like_list':json.dumps(like_list),
		#'num_list':json.dumps(num_list),
		'topname1':result[temp_list[0]][1],'topsex1':result[temp_list[0]][2],'topage1':result[temp_list[0]][3],'topaddress1':result[temp_list[0]][4],
		'topname2':result[temp_list[1]][1],'topsex2':result[temp_list[1]][2],'topage2':result[temp_list[1]][3],'topaddress2':result[temp_list[1]][4],
		'topname3':result[temp_list[2]][1],'topsex3':result[temp_list[2]][2],'topage3':result[temp_list[2]][3],'topaddress3':result[temp_list[2]][4],
		'topname4':result[temp_list[3]][1],'topsex4':result[temp_list[3]][2],'topage4':result[temp_list[3]][3],'topaddress4':result[temp_list[3]][4],
		'num1':num_list[0],'num2':num_list[1],'num3':num_list[2],'num4':num_list[3],'num5':num_list[4],'num6':num_list[5],'num7':num_list[6],
		'num8':num_list[7],'num9':num_list[8],'num10':num_list[9],'num11':num_list[10],'num12':num_list[11],'num13':num_list[12],
		'num14':num_list[13],'num15':num_list[14],'num16':num_list[15],'num17':num_list[16],'num18':num_list[17],'num19':num_list[18],
		'num20':num_list[19],'num21':num_list[20],'num22':num_list[21],'num23':num_list[22],'num24':num_list[23],
		'username':request.session.get('user_name',default=None)}))
		#else:
			#html=t.render(template.Context({'current_date':now,'state':request.session.get('state',default=None)}))
		return HttpResponse(html)
	else:
		fp.close()
		html=t.render(template.Context({'current_date':now}))
		return HttpResponse(html)
#def dating_detail(request):
def like(request):
	name=request.POST.get('name')
	username=request.POST.get('username')
	result = {}  
	result['code'] = 0  
	result['message'] = '已经赞过'  
	cursor.execute("SELECT * FROM gayest.liketable where likename = '%s'and username='%s'"%(name,username))
	count=cursor.fetchone()
	if(count!=None):
		return HttpResponse(json.dumps(result), content_type="application/json") 
	else:
		if(name!=None and username!=None):
			cursor.execute("INSERT INTO liketable(likename,username) VALUES('%s','%s')"%(name,username))
			db.commit()
			result['code'] = 1 
			result['message'] = 'like success'
		else:   
			result['message'] = 'name and username can not null' 
		return HttpResponse(json.dumps(result), content_type="application/json") 
