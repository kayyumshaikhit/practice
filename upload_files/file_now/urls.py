from django.urls import path 
from . import views 


urlpatterns = [
    path("",views.list),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("upload/",views.post,name="create")
]