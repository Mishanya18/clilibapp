from django.urls import path
from django.contrib.auth.views import LoginView
from .import views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView



urlpatterns = [
    path('', RedirectView.as_view(url='login'), name='start_url'),
    path("login/", LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login_url'),
    path("clients/", login_required(views.ClientView.as_view()), name='clients_url'),
    path("clients/create", login_required(views.ClientCreateOrgView.as_view()), name='clients_create_url'),
    path("client/<int:pk>/spokesmans", login_required(views.ClientCreateSpokesmanView.as_view()), name='clients_create_spokesmans_url'),
    path("client/<int:pk>/services/create", login_required(views.ClientCreateServiceView.as_view()), name='clients_create_services_url'),
    path("client/<int:pk>/services/update", login_required(views.ClientUpdateServiceView.as_view()), name='clients_update_services_url'),
    path("client/<int:pk>/delete", login_required(views.ClientDeleteOrgView.as_view()), name='clients_delete_url'),
    path("client/<int:pk>/update", login_required(views.ClientUpdateOrgView.as_view()), name='clients_update_url'),
    path("client/<int:pk>/", login_required(views.ClientDetailView.as_view()), name='client_detail_url'),
    path("spokesmans", login_required(views.SpokesmanView.as_view()), name='spokesmans_url'),
    path("spokesmans/create", login_required(views.SpokesmanCreateView.as_view()), name='spokesmans_create_url'),
    path("spokesmans/<int:pk>/update", login_required(views.SpokesmanUpdateView.as_view()), name='spokesmans_update_url'),
    path("spokesmans/<int:pk>/delete", login_required(views.SpokesmanDeleteView.as_view()), name='spokesmans_delete_url'),
    path("services", login_required(views.ServiceView.as_view()), name='services_url'),
    path("services/create", login_required(views.ServTypeCreateView.as_view()), name='services_create_url'),
    path("services/<int:pk>/update", login_required(views.ServTypeUpdateView.as_view()), name='services_update_url'),
    path("services/<int:pk>/delete", login_required(views.ServTypeDeleteView.as_view()), name='services_delete_url'),
    path("managers", login_required(views.ManagerView.as_view()), name='managers_url'),
    path("managers/create", login_required(views.ManagerCreateView.as_view()), name='managers_create_url'),
    path("managers/<int:pk>/update", login_required(views.ManagerUpdateView.as_view()), name='managers_update_url'),
    path("managers/<int:pk>/delete", login_required(views.ManagerDeleteView.as_view()), name='managers_delete_url'),
]
