from django.urls import path 
from . import views

urlpatterns = [
    path("",views.upload_video),
    path("getall/",views.get_all_file),
    path("getfile/<int:id>/",views.get_file),
    path("drop/<int:id>/",views.drop),
    path("renamefile/<int:id>/",views.rename_file)
]
