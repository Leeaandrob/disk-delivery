#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse as r
from django.contrib.auth.models import Group

from diskdelivery.clientes.models import Cliente
from diskdelivery.clientes.forms import ClienteForm

def cadastro(request):
    '''
    @view para cadastrar um novo cliente
    '''
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = obj.email
            obj.set_password(obj.set_password)
            obj.save()
            grupo = Group.objects.get(name='Cliente')
            obj.groups.add(grupo)
            obj.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"cadastro.html",{'form':form})
    else:
        return render(request,"cadastro.html",{'form':ClienteForm()})
