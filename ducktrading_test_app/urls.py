from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('returntozero', views.returntozero),
    path('settings', views.settings),
    path('buy', views.buy),
    path('sell', views.sell),
    path('gainloss', views.gainloss),

]
