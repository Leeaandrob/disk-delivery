# coding: utf-8

from django import forms
from diskdelivery.comidas.models import Comida
from django.core.exceptions import ValidationError

class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ('nome',)
        widgets ={
        	'nome': forms.TextInput(attrs={'class':'form-control','size':30}),
        }

    def clean_nome(self):
        '''
            @clean_name: Transforma o nome em maiusculo
        '''
        return self.cleaned_data['nome'].upper()

