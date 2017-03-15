"""Gayest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^makefriends','makefriends.views.hello'),
	url(r'^$','index.views.gayest'),
	url(r'^dating.html','makefriends.views.hello'),
	url(r'^index.html','index.views.gayest'),
	url(r'^news.html','news.views.news'),
	url(r'^news','news.views.news'),
	url(r'^party.html','party.views.party'),
	url(r'^party','party.views.party'),
	url(r'^dating','makefriends.views.hello'),
	#url(r'^single.html','news_detail.views.news_detail'),
	url(r'^single','news_detail.views.news_detail'),
	url(r'^login','login.views.login'),
	url(r'^login.html','login.views.login'),
	url(r'^check-action','login.views.check'),
	url(r'^register.html','login.views.register'),
	url(r'^register','login.views.register'),
	url(r'^submit-action','login.views.submitregister'),
	url(r'^logout-action','login.views.logout'),
	#url(r'^dating/$','makefriends.views.dating_detail'),
	url(r'^dianzan','makefriends.views.like'),
	url(r'^jiaru','party.views.ooo'),
	url(r'^ajax-action','party.views.load'),
	url(r'^contact.html','index.views.contact'),
	url(r'^contact','index.views.contact'),
	url(r'^feedback-action','index.views.feedback'),
	url(r'^comment-action','news_detail.views.comment'),
	#url(r'^subparty.html','party.views.party_detail'),
	url(r'^subparty','party.views.party_detail'),
	url(r'^subparty/$','party.views.party_detail'),
	url(r'^single/$','news_detail.views.news_detail'),]