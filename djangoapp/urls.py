#app-->create a python file urls.py

from django.urls import path
from .views import *

urlpatterns=[
    path('first/',first),
    path('second/',second),
    path('third/',third),
    path('project/',des),
    path('reg/',reg),
    path('login/',login),
    # path('index/',index),
    path('fileupload/',fileupload),
    path('emp_reg/',emp_reg),
    path('search_employee/',search_employee),
    path('product_detail/',product_detail),
    path('product_check/',product_check),
    path('fileupload3/',fileupload3),
    path('checkbox/',checkbox),
    path('display/',display),
    path('imgdisplay/',imgdisplay),
    path('addisplay/',addisplay),
    path('updatedata/<int:id>',update_data),
    path('empupdate/<int:id>',emp_update),
    path('imgupdate/<int:id>',img_update),
    path('avpupdate/<int:id>',avp_update),
    path('delete/<int:id>',delete_reg),
    path('delemp/<int:id>',delete_employee),
    path('imgdel/<int:id>',del_image),
    path('avpdel/<int:id>',del_avp),
    path('autuser/',userregistration),
    path('atuuser/',userregis),
    path('custom_login/',custom_login),


]