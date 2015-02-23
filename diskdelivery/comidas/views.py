#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse as r
from diskdelivery.comidas.models import Comida
from diskdelivery.comidas.forms import ComidaForm


def comida_lista(request):

	return render(request,"comida_lista.html",{'comidas':Comida.objects.all().order_by('nome')})

def comida_nova(request):
	'''
		@comida_nova: View para cadastrar um novo tipo de comida
	'''

	if request.method == 'POST':
		form = ComidaForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return HttpResponseRedirect(r('comidas:comida_lista'))
		return render(request,"comida_nova.html",{'form':form})
	else:
		return render(request,"comida_nova.html",{'form':ComidaForm()})
	
def comida_editar(request,comida_id):
	'''
		@comid_editar: View para editar os dados de uma comida
	'''
	comida = get_object_or_404(Comida,id=comida_id)
	if request.method == 'POST':
		form = ComidaForm(request.POST,instance=comida)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return HttpResponseRedirect(r('comidas:comida_lista'))
		return render(request,"comida_editar.html",{'form':form})
	else:
		return render(request,"comida_editar.html",{'form':ComidaForm(instance=comida)})