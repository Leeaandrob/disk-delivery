# coding: utf-8

from django import forms
from diskdelivery.cardapios.models import ItemCardapio
from diskdelivery.comidas.models import Comida
from diskdelivery.restaurantes.models import Restaurante
from django.core.exceptions import ValidationError
from django.forms.widgets import Select

class ItemCardapioForm(forms.ModelForm):
    class Meta:
        model = ItemCardapio
        fields = ('nome','descricao','preco','comida')
        widgets ={
        	'nome': forms.TextInput(attrs={'class':'form-control','size':30}),
            'descricao': forms.Textarea(attrs={'class':'form-control','size':30}),
            'preco': forms.TextInput(attrs={'class':'form-control','size':30}),
            'comida': Select(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemCardapioForm, self).__init__(*args, **kwargs)  
        restaurante = Restaurante.objects.get(id=kwargs['initial']['restaurante_id'])
        self.fields['comida'].queryset = restaurante.comidas


    def clean_nome(self):
        '''
            @clean_name: Transforma o nome em maiusculo
        '''
        return self.cleaned_data['nome'].upper()

