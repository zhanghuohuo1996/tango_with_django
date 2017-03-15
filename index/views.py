#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect
from django import template
import datetime
from index.models import Indexmodel
from index.models import Feedback
import MySQLdb

# Create your views here.
def gayest(request):
    now=datetime.datetime.now()
    fp=open(r'E:\mysite\Gayest\makefriends\templates\index.html')
    t=template.Template(fp.read())
    request.session['state']=False
    if(request.session['state']==True):        
        user_list=Indexmodel.objects.all()
        fp.close()
        html1=t.render(template.Context({'current_date':now,'user1':user_list[0],'isLogin':True,
        'user2':user_list[1],'user3':user_list[2],'user4':user_list[3],'user5':user_list[4],
        'user6':user_list[5],'user7':user_list[6],'user8':user_list[7],'user9':user_list[8],
        'user10':user_list[9],'user11':user_list[10],'user12':user_list[11],'state':request.session.get('state',default=None),'username':request.session.get('user_name',default=None)}))
        html=HttpResponse(html1)
        return html
    else:
        user_list=Indexmodel.objects.all()
        fp.close()
        html1=t.render(template.Context({'current_date':now,'user1':user_list[0],'isLogin':True,
        'user2':user_list[1],'user3':user_list[2],'user4':user_list[3],'user5':user_list[4],
        'user6':user_list[5],'user7':user_list[6],'user8':user_list[7],'user9':user_list[8],
        'user10':user_list[9],'user11':user_list[10],'user12':user_list[11],'state':request.session.get('state',default=None)}))
        html=HttpResponse(html1)
        return html 
def contact(request):
    now=datetime.datetime.now()
    fp=open(r'E:\mysite\Gayest\makefriends\templates\contact.html')
    t=template.Template(fp.read())
    if(request.session['state']==True):        
        fp.close()
        html1=t.render(template.Context({'current_date':now,'state':request.session.get('state',default=None),'username':request.session.get('user_name',default=None)}))
        html=HttpResponse(html1)
        return html
    else:
        fp.close()
        html1=t.render(template.Context({'current_date':now,'state':request.session.get('state',default=None)}))
        html=HttpResponse(html1)
        return html 
def feedback(request):
	advice=request.POST.get('advice','')
	name=request.POST.get('name','')
	number=request.POST.get('phoneNumber','')
	email=request.POST.get('email','')
	db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest")
	db.set_character_set('utf8')  
	cursor=db.cursor()
	sql='INSERT INTO feedback(advice,name,number,email)values("%s","%s","%s","%s")'%(advice,name,number,email)
	cursor.execute(sql)
	db.commit()
	db.close()
	return HttpResponseRedirect("index.html")
	# now=datetime.datetime.now()
	# fp=open(r'E:\mysite\Gayest\makefriends\templates\index.html')
	# t=template.Template(fp.read())
	# fp.close()
	# html=t.render(template.Context({'current_date':now}))
	# return HttpResponse(html)	
