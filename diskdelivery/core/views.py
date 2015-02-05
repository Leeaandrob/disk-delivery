#coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse as r
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import Group,User
#coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse as r
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import Group,User


def inicio_site(request):
	'''
		@inicio_site: View para renderizar a página inicial do site
	'''
	return render(request,"inicio_site.html")

@login_required
def home(request):
	'''
		@home: View para acesso da interface adminsitrativa
	'''
	return render(request,"home.html")
