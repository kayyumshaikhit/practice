from django.shortcuts import get_object_or_404, redirect, render
from .models import fileModel
from .serializers import fileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from .forms import fileModelForm
# Create your views here.

def list(request):
    instance = fileModel.objects.all()
    serializer = fileSerializer(instance=instance,many=True)
    return render(request,"show.html",{"data" : instance})

def delete(request,id):
        file = get_object_or_404(fileModel,id=id)
        if file is not None:
              file.delete()
              return redirect("/")
        return render(request,"sample.html",{ "file_name" : file.file.name })

@parser_classes([MultiPartParser, FormParser])
def post(request):
    if request.method == "POST":
        form = fileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = fileModelForm()
    return render(request, 'form.html', {'form': form})