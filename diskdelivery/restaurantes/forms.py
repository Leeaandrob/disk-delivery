# coding: utf-8

from django import forms
from diskdelivery.restaurantes.models import Restaurante
from django.core.exceptions import ValidationError

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ('razao_social','email','telefone','endereco','bairro','municipio','estado','cnpj','password','comidas')
        widgets ={
        	'razao_social': forms.TextInput(attrs={'class':'form-control','size':30}),
            'email': forms.TextInput(attrs={'class':'form-control','size':30}),
            'telefone': forms.TextInput(attrs={'class':'form-control','size':30}),
            'endereco': forms.TextInput(attrs={'class':'form-control','size':30}),
            'bairro': forms.TextInput(attrs={'class':'form-control','size':30}),
            'municipio': forms.TextInput(attrs={'class':'form-control','size':30}),
            'estado': forms.TextInput(attrs={'class':'form-control','size':30}),
            'cnpj': forms.TextInput(attrs={'class':'form-control','size':30}),
            'password': forms.TextInput(attrs={'class':'form-control','size':30}),
            'comidas': forms.CheckboxSelectMultiple(attrs={'class':'form-inline'}),
        }

    def clean_nome(self):
        '''
            @clean_name: Transforma o nome em maiusculo
        '''
        return self.cleaned_data['nome'].upper()


class RestauranteFormEditar(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ('razao_social','email','telefone','endereco','bairro','municipio','estado','cnpj','comidas')
        widgets ={
            'razao_social': forms.TextInput(attrs={'class':'form-control','size':30}),
            'email': forms.TextInput(attrs={'class':'form-control','size':30}),
            'telefone': forms.TextInput(attrs={'class':'form-control','size':30}),
            'endereco': forms.TextInput(attrs={'class':'form-control','size':30}),
            'bairro': forms.TextInput(attrs={'class':'form-control','size':30}),
            'municipio': forms.TextInput(attrs={'class':'form-control','size':30}),
            'estado': forms.TextInput(attrs={'class':'form-control','size':30}),
            'cnpj': forms.TextInput(attrs={'class':'form-control','size':30}),
            'comidas': forms.CheckboxSelectMultiple(attrs={'class':'form-inline'}),
        }

    def clean_nome(self):
        '''
            @clean_name: Transforma o nome em maiusculo
        '''
        return self.cleaned_data['nome'].upper()

