# coding: utf-8

from django import forms
from diskdelivery.clientes.models import Cliente
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    password2 = forms.CharField(label='Repita sua senha',error_messages={'required': 'Preenchimento Obrigatório'},
                         widget=forms.PasswordInput(attrs={'class':'form-control','size': 20}))

    class Meta:
        model = Cliente
        fields = ('first_name','last_name','email','telefone','endereco','bairro','municipio','estado','password',)
        widgets ={
            'first_name': forms.TextInput(attrs={'class':'form-control','size':30}),
            'last_name': forms.TextInput(attrs={'class':'form-control','size':30}),
            'email': forms.TextInput(attrs={'class':'form-control','size':30}),
            'telefone': forms.TextInput(attrs={'class':'form-control','size':30}),
            'endereco': forms.TextInput(attrs={'class':'form-control','size':30}),
            'bairro': forms.TextInput(attrs={'class':'form-control','size':30}),
            'municipio': forms.TextInput(attrs={'class':'form-control','size':30}),
            'estado': forms.TextInput(attrs={'class':'form-control','size':30}),
            'cnpj': forms.TextInput(attrs={'class':'form-control','size':30}),
            'password': forms.PasswordInput(attrs={'class':'form-control','size':30}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Confirme seu senha")
        if password1 != password2:
            raise forms.ValidationError("As senha estão diferentes")
        return password2