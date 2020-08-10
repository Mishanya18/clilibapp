from django.urls import path

from .import views



urlpatterns = [
    path("", views.ClientView.as_view(), name='clients_url'),
    path("clients/create", views.ClientCreateOrgView.as_view(), name='clients_create_url'),
    path("client/<int:pk>/spokesmans", views.ClientCreateSpokesmanView.as_view(), name='clients_create_spokesmans_url'),
    path("client/<int:pk>/services/create", views.ClientCreateServiceView.as_view(), name='clients_create_services_url'),
    path("client/<int:pk>/services/update", views.ClientUpdateServiceView.as_view(), name='clients_update_services_url'),
    path("client/<int:pk>/delete", views.ClientDeleteOrgView.as_view(), name='clients_delete_url'),
    path("client/<int:pk>/update", views.ClientUpdateOrgView.as_view(), name='clients_update_url'),
    path("client/<int:pk>/", views.ClientDetailView.as_view(), name='client_detail_url'),
    path("spokesmans", views.SpokesmanView.as_view(), name='spokesmans_url'),
    path("spokesmans/create", views.SpokesmanCreateView.as_view(), name='spokesmans_create_url'),
    path("spokesmans/<int:pk>/update", views.SpokesmanUpdateView.as_view(), name='spokesmans_update_url'),
    path("spokesmans/<int:pk>/delete", views.SpokesmanDeleteView.as_view(), name='spokesmans_delete_url'),
    path("services", views.ServiceView.as_view(), name='services_url'),
    path("services/create", views.ServTypeCreateView.as_view(), name='services_create_url'),
    path("services/<int:pk>/update", views.ServTypeUpdateView.as_view(), name='services_update_url'),
    path("services/<int:pk>/delete", views.ServTypeDeleteView.as_view(), name='services_delete_url'),
    path("managers", views.ManagerView.as_view(), name='managers_url'),
    path("managers/create", views.ManagerCreateView.as_view(), name='managers_create_url'),
    path("managers/<int:pk>/update", views.ManagerUpdateView.as_view(), name='managers_update_url'),
    path("managers/<int:pk>/delete", views.ManagerDeleteView.as_view(), name='managers_delete_url'),
]
