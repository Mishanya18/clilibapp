from django import forms
from .models import Manager, ServType, Spokesman, Client, Service

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['name', 'sername', 'telephone', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName', 'type': 'text'}),
            'sername': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputSername', 'type': 'text'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputTelephone', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'type': 'email'})
        }

class ServTypeForm(forms.ModelForm):
    class Meta:
        model = ServType
        fields = ['title', 'unit_of_measure', 'short_name']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputTitle', 'type': 'text'}),
            'unit_of_measure': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputUnit_of_measure', 'type': 'text'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputShort_name', 'type': 'text'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['amount', 'offered', 'client', 'type']

        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAmount'}),
            'offered': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'inputOffered'}),
            'client': forms.Select(attrs={'class': 'form-control', 'id': 'inputClient'}),
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'inputType'})
        }

class SpokesmanForm(forms.ModelForm):
    class Meta:
        model = Spokesman
        fields = ['name', 'sername', 'telephone', 'email', 'client']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName'}),
            'sername': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputSername'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputTelephone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail'}),
            'client': forms.Select(attrs={'class': 'form-control', 'id': 'inputClient'})
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['title', 'contract_number', 'test', 'stuff', 'manager', 'orgname']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputTitle'}),
            'contract_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputContract_number'}),
            'test': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'inputTest'}),
            'stuff': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'inputStuff'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'id': 'inputManager'}),
            'orgname': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputOrgname'})
        }
