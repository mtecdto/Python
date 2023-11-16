"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import home, form, create, view, edit, update,delete,backup,deleteAll,insertKeys,insertKeys2,atualizar_valores,insertkeys3,form2,inserir_chaves,duplicadas,export_data_to_csv,export_data_to_csv_duplicados,store,createLogin,painel,dologin,logouts,estoque_keys_status_disponível,criar_quantidade_maquinas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('form/',form, name='form'),
    path('criar_quantidade_maquinas/',criar_quantidade_maquinas, name='criar_quantidade_maquinas'),
    path('painel/',painel, name='painel'),
    path('dologin/',dologin, name='dologin'),
    path('logouts/', logouts, name='logouts'),
    path('createLogin/',createLogin, name='createLogin'),
    path('store/', store, name='store'),
    path('form2/', form2, name='form2'),
    path('create/',create, name='create'),
    path('view/<int:pk>/',view, name='view'),
    path('edit/<int:pk>/',edit, name='edit'),
    path('update/<int:pk>/',update, name='update'),
    path('delete/<int:pk>/',delete, name='delete'),
    path('backup/',backup, name='backup'),
    path('deleteAll/', deleteAll, name='deleteAll'),
    path('insertKeys/', insertKeys, name='insertKeys'),
    path('insertKeys2/', insertKeys2, name='insertKeys2'),
    path('atualizar_valores/', atualizar_valores, name='atualizar_valores'),
    path('insertkeys3/', insertkeys3, name='insertkeys3'),
    path('inserir_chaves/', inserir_chaves, name='inserir_chaves'),
    path('duplicadas/', duplicadas, name='duplicadas'),
    path('export_data_to_csv/', export_data_to_csv, name='export_data_to_csv'),
    path('export_data_to_csv_duplicados/', export_data_to_csv_duplicados, name='export_data_to_csv_duplicados'),
    path('estoque_keys_status_disponível/', estoque_keys_status_disponível, name='estoque_keys_status_disponível'),



]




