from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django import template
import datetime
from login.models import Loginmodel
from makefriends.models import Datingmodel
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import logging
from django.shortcuts import render_to_response
@csrf_exempt
# Create your views here.
def login(request):
    now=datetime.datetime.now()
    fp=open(r'E:\mysite\Gayest\makefriends\templates\login.html')
    t=template.Template(fp.read())
    fp.close()
    html=t.render(template.Context({'current_date':now}))
    return HttpResponse(html)
def check(request):
    username=request.POST.get('userName','')
    password1=request.POST.get('password','')
    db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest")
    cursor=db.cursor()
    user_list=Loginmodel.objects.all()
    cursor.execute("SELECT * FROM gayest.loginmodel where user = '%s'and password='%s'"%(username,password1))
    result=cursor.fetchone()
    #logging.debug(password1)
    #for i in user_list:
    if(result!=None):
        #request.seesion.set_expiry(0)
        request.session['state']=True
        request.session['user_name']=username
        #request.seesion['pass_word']=password1
        now=datetime.datetime.now()
        #fp=open(r'E:\mysite\Gayest\makefriends\templates\dating.html')
        #t=template.Template(fp.read())
        #fp.close()
        #html=t.render(template.Context({'current_date':now,'state':True,'username':username}))
        #return HttpResponse(html)
        #return render_to_response('dating.html')
        return HttpResponseRedirect('dating.html')
    else:
        now=datetime.datetime.now()
        fp=open(r'E:\mysite\Gayest\makefriends\templates\login.html')
        t=template.Template(fp.read())
        fp.close()
        html=t.render(template.Context({'current_date':now}))
        return HttpResponse(html)
def register(request):
    now=datetime.datetime.now()
    fp=open(r'E:\mysite\Gayest\makefriends\templates\register.html')
    t=template.Template(fp.read())
    fp.close()
    html=t.render(template.Context({'current_date':now}))
    return HttpResponse(html)
def submitregister(request):
    username=request.POST.get('userName','')
    password1=request.POST.get('password','')
    db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest")
    cursor=db.cursor()
    if(username!=None and password1!=None):
        sql='INSERT INTO loginmodel(user,password)values("%s","%s")'%(username,password1)
        cursor.execute(sql)
        db.commit()
        db.close()
        now=datetime.datetime.now()
        fp=open(r'E:\mysite\Gayest\makefriends\templates\login.html')
        t=template.Template(fp.read())
        fp.close()
        html=t.render(template.Context({'current_date':now}))
        return HttpResponse(html)
    else:
        now=datetime.datetime.now()
        fp=open(r'E:\mysite\Gayest\makefriends\templates\register.html')
        t=template.Template(fp.read())
        error="please input!"
        fp.close()
        html=t.render(template.Context({'current_date':now,'error':error}))
        return HttpResponse(html)
    #logging.debug(password1)
    #for i in user_list:
    #db=MySQLdb.connect(host="localhost",user="root",passwd="789789",db="gayest")
    #cursor=db.cursor()
    #for i in range(1,100):
      #  sql='INSERT INTO datingmodel(name,sex,age,address,image)values("%s","%s","%s","%s","%s")'%("aaa","male","23","China/Beijing/chaoyang","../../static/images/p12.jpg")
     #   cursor.execute(sql)
    #db.commit()
   # db.close()
    
def logout(request):
    request.session['state']=False
    del request.session['user_name']
    #del request.session['pass_word']
    fp=open(r'E:\mysite\Gayest\makefriends\templates\index.html')
    t=template.Template(fp.read())
    fp.close()
    now=datetime.datetime.now()
    html=t.render(template.Context({'current_date':now}))
    return HttpResponse(html)