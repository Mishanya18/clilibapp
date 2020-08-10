from django.contrib import admin
from .models import Client, Manager, Service, ServType, Spokesman

# Register your models here.
admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Service)
admin.site.register(ServType)
admin.site.register(Spokesman)
