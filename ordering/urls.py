
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('completeorder/<id>', views.completeorder, name='Complete Order'),
    path('undocomplete/<id>', views.undocomplete, name='Complete Order'),
]