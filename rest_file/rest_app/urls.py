from django.urls import path
from . import views 


urlpatterns = [
    path("",views.fileupload,name="upload"),
    path("getfile/",views.getfile),
    path("deletefile/<int:id>/",views.deletefile),
    path("updatefile/<int:id>/",views.updatefile)
]
