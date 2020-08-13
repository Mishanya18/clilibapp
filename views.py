from django.shortcuts import render, redirect
from django import forms
from django.views.generic.base import View
from .models import Client, Spokesman, Service, Manager, ServType
from .forms import ManagerForm, ServTypeForm, SpokesmanForm, ClientForm, ServiceForm
from .utils import *
# Create your views here.


class ClientViewAll(View):
    """Список клиентов"""
    template = "clilib/clients/clients_grid.html"
    logik_filter = ""
    def get(self, request):
        if self.logik_filter=="test":
            clients = Client.objects.filter(test=True)
        elif self.logik_filter=="all":
            clients = Client.objects.all()
        elif self.logik_filter=="staff":
            clients = Client.objects.filter(stuff=True)
        else:
            clients = Client.objects.all()
        companies={}
        for client in clients:
            companies[client]=Spokesman.objects.filter(client = client)
        return render(request, self.template, {"clients_list": clients, "companies": companies})

class ClientDetailView(View):
    """Список клиентов"""
    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        spokesmans = Spokesman.objects.filter(client = client)
        service_list = Service.objects.filter(client__id = pk)
        return render(request, "clilib/clients/client_detail.html", {'client': client, 'service_list': service_list, 'spokesmans': spokesmans})

class ClientCreateOrgView(View):
    """Создание нового клиента с редиректом на создание представителей"""
    def get(self, request):
        form = ClientForm()
        return render(request, "clilib/clients/clients_create.html", {"form": form})

    def post(self, request):
        bound_form = ClientForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj.get_spokersman_add_url())
        return render(request, "clilib/clients/clients_create.html", {"form": bound_form})

class ClientDeleteOrgView(ObjectDeleteMixin, View):
    """Удаление клиента"""
    model = Client
    template = "clilib/clients/clients_delete.html"
    redirect_url = 'clients_url'

class ClientUpdateOrgView(ObjectUpdateMixin, View):
    """Изменение клиента"""
    model = Client
    form_model = ClientForm
    template = "clilib/clients/clients_update.html"
    redirect_url = 'clients_url'

class ClientCreateSpokesmanView(View):
    """Создание нового представителя клиента с редиректом на создание услуг"""
    def get(self, request, pk):
        form = SpokesmanForm()
        form.fields['client'] = forms.ModelChoiceField(queryset = Client.objects.filter(id=pk), empty_label = None)
        form.fields['client'].widget.attrs.update({'class': 'form-control', 'id': 'inputClient'})
        client = Client.objects.get(id=pk)
        return render(request, "clilib/clients/clients_spokesmans_create.html", {"form": form, "client": client})

    def post(self, request, pk):
        bound_form = SpokesmanForm(request.POST)
        client = Client.objects.get(id=pk)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(client.get_service_add_url())
        #return render(request, "clilib/clients/clients_spokesmans_create.html", {"form": bound_form})
        return redirect('clients_create_spokesmans_url', pk = pk)

class ClientCreateServiceView(View):
    """Создание новых услуг"""
    def get(self, request, pk):
        form = ServiceForm()
        form.fields['client'] = forms.ModelChoiceField(queryset = Client.objects.filter(id=pk), empty_label = None)
        form.fields['client'].widget.attrs.update({'class': 'form-control', 'id': 'inputClient'})

        client = Client.objects.get(id=pk)
        return render(request, "clilib/clients/clients_services_create.html", {"form": form, "client": client})

    def post(self, request, pk):
        bound_form = ServiceForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('clients_url')
        return render(request, "clilib/clients/clients_services_create.html", {"form": bound_form})

class ClientUpdateServiceView(View):
    """Изменение услуг"""
    def get(self, request, pk):
        form = ServiceForm()
        form.fields['client'] = forms.ModelChoiceField(queryset = Client.objects.filter(id=pk), empty_label = None)
        form.fields['client'].widget.attrs.update({'class': 'form-control', 'id': 'inputClient'})

        client = Client.objects.get(id=pk)
        return render(request, "clilib/clients/clients_services_update.html", {"form": form, "client": client})

    def post(self, request, pk):
        bound_form = ServiceForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('client_detail_url', pk = pk)
        return render(request, "clilib/clients/clients_services_update.html", {"form": bound_form})

class SpokesmanView(View):
    """Список представителей"""
    def get(self, request):
        spokesmans = Spokesman.objects.all()
        return render(request, "clilib/spokesmans/spokesmans_list.html", {"spokesmans_list": spokesmans})

class SpokesmanCreateView(ObjectCreateMixin, View):
    """Создание нового представителя клиента"""
    form_model = SpokesmanForm
    template = "clilib/spokesmans/spokesmans_create.html"
    redirect_url = 'spokesmans_url'

class SpokesmanUpdateView(ObjectUpdateMixin, View):
    """Изменение представителя клиента"""
    model = Spokesman
    form_model = SpokesmanForm
    template = "clilib/spokesmans/spokesmans_update.html"
    redirect_url = 'spokesmans_url'

class SpokesmanDeleteView(ObjectDeleteMixin, View):
    """Удаление представителя клиента"""
    model = Spokesman
    template = "clilib/spokesmans/spokesmans_delete.html"
    redirect_url = 'spokesmans_url'

class ServiceView(View):
    """Список услуг"""
    def get(self, request):
        services = ServType.objects.all()
        return render(request, "clilib/services/services_list.html", {"services_list": services})

class ServTypeCreateView(ObjectCreateMixin, View):
    """Создание нового типа услуги"""
    form_model = ServTypeForm
    template = "clilib/services/servtype_create.html"
    redirect_url = 'services_url'

class ServTypeUpdateView(ObjectUpdateMixin, View):
    """Изменение типа услуги"""
    model = ServType
    form_model = ServTypeForm
    template = "clilib/services/servtype_update.html"
    redirect_url = 'services_url'

class ServTypeDeleteView(ObjectDeleteMixin, View):
    """Удаление типа услуги"""
    model = ServType
    template = "clilib/services/servtype_delete.html"
    redirect_url = 'services_url'

class ManagerView(View):
    """Список менеджеров"""
    def get(self, request):
        managers = Manager.objects.all()
        return render(request, "clilib/managers/managers_list.html", {"managers_list": managers})

class ManagerCreateView(ObjectCreateMixin, View):
    """Создание нового менеджера"""
    form_model = ManagerForm
    template = "clilib/managers/manager_create.html"
    redirect_url = 'managers_url'

class ManagerUpdateView(ObjectUpdateMixin, View):
    """Изменение менеджера"""
    model = Manager
    form_model = ManagerForm
    template = "clilib/managers/manager_update.html"
    redirect_url = 'managers_url'

class ManagerDeleteView(ObjectDeleteMixin, View):
    """Удаление менеджера"""
    model = Manager
    template = "clilib/managers/manager_delete.html"
    redirect_url = 'managers_url'
