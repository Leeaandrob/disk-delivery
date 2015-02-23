#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse as r
from diskdelivery.cardapios.models import ItemCardapio
from diskdelivery.cardapios.forms import ItemCardapioForm
from diskdelivery.restaurantes.models import Restaurante

def cardapio_lista(request):
	'''
		@View para renderizar o cardapio de um restaurante
	'''

	restaurante = Restaurante.objects.get(id=request.user.id)

	cardapio = ItemCardapio.objects.filter(restaurante=restaurante)
	return render(request,"cardapio_lista.html",{'cardapio':cardapio,'restaurante':restaurante})

def itemcardapio_novo(request):
	'''
		@comida_nova: View para cadastrar um novo tipo de comida
	'''
	restaurante = Restaurante.objects.get(id=request.user.id)
	
	if request.method == 'POST':
		form = ItemCardapioForm(request.POST,initial={'restaurante_id':restaurante.id})
		if form.is_valid():
			obj = form.save(commit=False)
			obj.restaurante = restaurante
			obj.save()
			return HttpResponseRedirect(r('cardapios:cardapio_lista'))
		return render(request,"item_cardapio_novo.html",{'form':form})
	else:
		return render(request,"item_cardapio_novo.html",{'form':ItemCardapioForm(initial={'restaurante_id': restaurante.id})})
	
def itemcardapio_editar(request,item_id):
	'''
		@comid_editar: View para editar os dados de uma comida
	'''
	item = get_object_or_404(ItemCardapio,id=item_id)
	restaurante = Restaurante.objects.get(id=request.user.id)
	if request.method == 'POST':
		form = ItemCardapioForm(request.POST,instance=item,initial={'restaurante_id':restaurante.id})
		if form.is_valid():
			obj = form.save(commit=False)
			obj.restaurante = restaurante
			obj.save()
			return HttpResponseRedirect(r('cardapios:cardapio_lista'))
		return render(request,"item_cardapio_editar.html",{'form':form})
	else:
		return render(request,"item_cardapio_editar.html",{'form':ItemCardapioForm(instance=item,initial={'restaurante_id':restaurante.id})})