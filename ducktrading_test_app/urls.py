from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('returntozero', views.returntozero),
    path('settings', views.settings),
    path('buy', views.buy),
    path('buy/<int:security_id>', views.buy),
    path('sell/<int:security_id>', views.sell),
    path('gainloss', views.gainloss),
    path('logout', views.logout),
    path('login', views.login),
    path('register', views.register),
    path('security/edit/<int:security_id>', views.edit), 
    # path('delete/<int:security_id>', views.delete),
    path('delete', views.delete),
    path('reset', views.reset),
    path('update/{{user_id}}', views.update),
    path('customer/<str:pk>/', views.customer),
    path('purchase/<int:security_id>', views.purchase),
    path('destory/<int:security_id>', views.destroy),
    path('sellsecurity/<int:security_id>', views.sellsecurity),
]


