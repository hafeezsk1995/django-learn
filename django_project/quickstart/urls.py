from django.urls import path
from . import views


urlpatterns = [
    path('jinja/', views.post_detail, name='home'),
    path('', views.home, name='home'),
    path('create', views.post_student, name='home'),
    path('update/<int:id>', views.update_student, name='home'),
    path('delete/<int:id>', views.delete_student, name='home'),
    path('generics/list', views.StudentList.as_view(), name='home'),
    path('generics/create', views.StudentCreate.as_view(), name='create'),
]