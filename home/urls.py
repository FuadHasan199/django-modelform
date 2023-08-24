from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home),
    path('show_task/',views.show_task,name='show_task'),
    path('add_task/',views.add_task,name='add_task'),
    path('edit_task/',views.edit_task,name='edit_task'),
    path('complete_task/',views.complete_task,name='complete_task'),
    path('modify_task/<int:id>',views.modify_task,name='modify_task'),
    path('delete_task/<int:id>',views.delete_task,name='delete_task'),
    path('completed_task/<int:id>',views.completed_task,name='completed_task'),
]
