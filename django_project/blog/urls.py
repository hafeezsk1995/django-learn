from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('about/', views.about, name='blog-about'),
    path('home/', views.home, name='blog-data'),
    path('check/', views.data, name='blog-home'),
    path('fileupload',views.FileUpload.as_view(),name='file-upload'),
    path('func_type_fileupload',views.file_upload_fun_type,name='file-upload'),
    path('update',views.MyModelOperations.as_view(),name='operations'),
    path('data_migration',views.DataMigration.as_view(),name='operations'),
    path('get_create',views.GetCreate.as_view(),name='operations'),
    path('get_data',views.Getdata.as_view(),name='operations'),
    path('django_api',views.my_model_api,name="django-calls-only"),
    path('check_one_to_api',views.One_One_Checking.as_view(),name="django-calls-only"),
    path('Update_One_One_checking',views.Update_One_One_checking.as_view(),name="django-calls-only"),
    path('get_one_check',views.Get_One_One_Checking.as_view(),name="django-calls-only"),
    path('delete_one_check',views.Delete_customer.as_view(),name="django-calls-only"),
    path('deleviry_post',views.DeleviryCreation.as_view(),name="django-calls-only"),
    path('many_post',views.ManyPost.as_view(),name="django-calls-only"),
    path('many_get',views.ManyGet.as_view(),name="django-calls-only"),
    path('ManyGetInterestsFromPersons',views.ManyGetInterestsFromPersons.as_view(),name="django-calls-only"),

    path('function_in_model',views.CheckFunInModels.as_view(),name="django-calls-only"),

    path('meta_check',views.check_meta,name='meta_check'),
    path('form_image_upload',views.form_image_upload,name='meta_check'),
    #check_request
    path('request_check',views.check_request,name='request_check'),
    path('ListWithDifferent',views.ListWithDifferent.as_view()),
    
]
