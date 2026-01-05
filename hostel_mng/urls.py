"""
URL configuration for hostel_mng project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from app1.views import hostel_details,hst_form,room_details,rom_form,std_form,std_details,compl_details,compl_form,pay_details,pay_form,visit_details,visit_form
from app1.views import hst_update,room_update,std_update,compl_update,visit_update,pay_update
from app1.views import hst_delete,room_delete,std_delete,compl_delete,visit_delete,pay_delete
from app1.views import dashboard,registration_form,login_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regi/',registration_form,name='regi'),
    path('',login_form,name='login101'),


    
    path('dash/', dashboard, name='dashboard'),
    path('hostel/',hostel_details,name='hostel'),
    path('hostel_form/',hst_form,name='hostel_form'),
    path('hst_update/<int:id>',hst_update,name='hst_update'),
    path('hst_delete/<int:id>',hst_delete,name='hst_delete'),

    path('room/',room_details,name='room'),
    path('room_form/',rom_form,name='room_form'),
    path('room_update/<int:id>',room_update,name='room_update'),
    path('room_delete/<int:id>',room_delete,name='room_delete'),

    path('std/',std_details,name='std'),
    path('std_form/',std_form,name='std_form'),
    path('std_update/<int:id>',std_update,name='std_update'),
    path('std_delete/<int:id>',std_delete,name='std_delete'),

    path('complaint/',compl_details,name='complaint'),
    path('complaint_form/',compl_form,name='complaint_form'),
    path('complaint_update/<int:id>',compl_update,name='compl_update'),
    path('complaint_delete/<int:id>',compl_delete,name='compl_delete'),

    path('visitors/',visit_details,name='visitor'),
    path('visitor_form/',visit_form,name='visitor_form'),
    path('visitor_update/<int:id>',visit_update,name='visit_update'),
    path('visitor_delete/<int:id>',visit_delete,name='visit_delete'),

    path('payment/',pay_details,name='pay'),
    path('payment_form/',pay_form,name='pay_form'),
    path('payment_update/<int:id>',pay_update,name='pay_update'),
    path('payment_delete/<int:id>',pay_delete,name='pay_delete'),
]
