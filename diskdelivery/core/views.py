#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse as r
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import Group,User

from diskdelivery.core.models import Pessoa

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

	usuario = request.user
	try:
		usuario = Pessoa.objects.get(id=request.user.id)
	except:
		pass

	return render(request,"home.html",{'pessoa':usuario})

def carregar(request):

    grupo_admin = Group.objects.create(name='Administrador')
    grupo_restaurante = Group.objects.create(name='Restaurante')
    grupo_cliente = Group.objects.create(name='Cliente')

    return HttpResponse("gerado")