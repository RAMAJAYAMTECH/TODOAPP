from typing import Pattern
from unicodedata import name
from django.urls import path
from todolist_app import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.todolist, name='todolist'),
    path('todoemp', views.todoemp, name='todoemp'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('view/<task_id>', views.view_task, name='view_task'),
    path('complete', views.complete_task, name='complete_task'),
    path('finish', views.finish_task, name='finish_task'),
    path('finish1/<task_id>', views.finish1_task, name='finish1_task'),
    path('success', views.success, name='success'),
    path('email1/<task_id>', views.email1, name='email1'),
    path('export', views.export, name='export'),

    path('export2', views.export2, name='export2'),
    path('email_updatetask/<id>', views.email_updatetask, name='email_updatetask'),
    path('email_remindertask/<id>', views.email_remindertask, name='email_remindertask'),
    
    path('arul', views.todolist1, name='todolist1'),
    path('ram', views.todolist2, name='todolist2'),
    path('akash', views.todolist3, name='todolist3'),
    path('Pavithra', views.todolist4, name='todolist4'),
    path('Hithesh', views.todolist5, name='todolist5'),
    path('kalai', views.todolist6, name='todolist6'),
    path('surya', views.todolist7, name='todolist7'),

    path('sms', views.sms, name='sms'),
    path('attendance',views.attendance,name='attendance'),
    path('gstmaster',views.gstmaster,name='gstmaster'),
    path('empdetails',views.empdetails,name='empdetails'),

    path('emp1',views.emp1,name='emp1'),
    path('emp2',views.emp2,name='emp2'),
    path('emp3',views.emp3,name='emp3'),
    path('emp4',views.emp4,name='emp4'),
    path('emp5',views.emp5,name='emp5'),
    path('emp6',views.emp6,name='emp6'),

    path('dailywork1',views.dailywork1,name='dailywork1'),
    path('dailywork2',views.dailywork2,name='dailywork2'),
    path('dailywork3',views.dailywork3,name='dailywork3'),
    path('dailywork4',views.dailywork4,name='dailywork4'),
    path('dailywork5',views.dailywork5,name='dailywork5'),
    path('dailyworkreport',views.dailyworkreport,name='dailyworkreport'),

    path('pdf',views.pdf,name='pdf'),
    path('pdff',views.pdff,name='pdff'),
    path('pdf1',views.pdf1,name='pdf1'),
    path('pdf2',views.pdf2,name='pdf2'),
    path('pdf3',views.pdf3,name='pdf3'),
    path('pdf4',views.pdf4,name='pdf4'),
    path('pdf5',views.pdf5,name='pdf5'),

    path('search',views.search,name='search'),
    path('sss',views.sss,name='sss'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('add',views.add,name='add'),
    
]

import execute
#path('', views.subscribe, name = 'subscribe'),  path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),