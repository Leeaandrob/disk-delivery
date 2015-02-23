#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse as r
from django.contrib.auth.models import Group
from diskdelivery.restaurantes.forms import RestauranteForm,RestauranteFormEditar
from diskdelivery.restaurantes.models import Restaurante


def restaurante_lista(request):

	return render(request,"restaurante_lista.html",{'restaurantes':Restaurante.objects.all()})

def restaurante_novo(request):
	'''
		@restaurante_novo: View para cadastrar um novo restaurante
	'''
	if request.method == 'POST':
		 form = RestauranteForm(request.POST)
		 if form.is_valid():
		 	obj = form.save(commit=False)
		 	obj.username = obj.email
		 	obj.set_password(obj.password)
		 	grupo = Group.objects.get(name='Restaurante')
		 	obj.save()
		 	obj.groups.add(grupo)
		 	obj.save()
		 	return HttpResponseRedirect(r('restaurantes:restaurante_lista'))
		 return render(request,"restaurante_novo.html",{'form':form})
	else:
		return render(request,"restaurante_novo.html",{'form':RestauranteForm()})


def restaurante_editar(request,restaurante_id):
	'''
		@restaurante_editar: view para editar os dados de um restaurante
	'''

	restaurante = get_object_or_404(Restaurante,id=restaurante_id)
	if request.method == 'POST':
		form = RestauranteFormEditar(request.POST,instance=restaurante)
		if form.is_valid():
			obj = form.save(commit=False)
		 	obj.save()
		 	form.save_m2m()
		 	return HttpResponseRedirect(r('restaurantes:restaurante_lista'))
		return render(request,"restaurante_editar.html",{'form':form})
	else:
		return render(request,"restaurante_editar.html",{'form':RestauranteFormEditar(instance=restaurante)})
