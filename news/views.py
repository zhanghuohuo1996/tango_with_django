from django.shortcuts import render
from django.http import HttpResponse,Http404
from django import template
import datetime
from news.models import Newsmodel
# Create your views here.
def news(request):
    now=datetime.datetime.now()
    fp=open(r'E:\mysite\Gayest\makefriends\templates\news.html')
    t=template.Template(fp.read())
    news_list=Newsmodel.objects.all()
    fp.close()
    if(request.session['state']==True):
        html=t.render(template.Context({'current_date':now,'news_list1':news_list[0],
        'news_list2':news_list[1],'news_list3':news_list[2],'state':request.session.get('state',default=None),'username':request.session.get('user_name',default=None)}))
        return HttpResponse(html)
    else:
        html=t.render(template.Context({'current_date':now,'news_list1':news_list[0],
        'news_list2':news_list[1],'news_list3':news_list[2]}))
        return HttpResponse(html)