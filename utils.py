from django.shortcuts import render, redirect
from .models import Client, Spokesman, Service, Manager
from .forms import ManagerForm
from django.shortcuts import get_object_or_404


class ObjectCreateMixin:
    form_model = None
    template = None
    redirect_url = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, {"form": form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(self.redirect_url)
        return render(request, self.template, {"form": bound_form})

class ObjectUpdateMixin:
    model = None
    form_model = None
    template = None
    redirect_url = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, id=pk)
        bound_form = self.form_model(instance=obj)
        return render(request, self.template, {"form": bound_form, self.model.__name__.lower(): obj})

    def post(self, request, pk):
        obj = get_object_or_404(self.model, id=pk)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(self.redirect_url)
        return render(request, self.template, {"form": bound_form})

class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, id=pk)
        return render(request, self.template, {self.model.__name__.lower(): obj})

    def post(self, request, pk):
        obj = get_object_or_404(self.model, id=pk)
        obj.delete()
        return redirect(self.redirect_url)
