import os
import stat
import time
import ctypes
from pathlib import Path
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from contextlib import suppress 
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from .models import FileModel
from .serializers import FileSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
# Create your views here.

@api_view(["POST"])
def upload_video(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Notice the 's' in errors and explicit HTTP 400 Bad Request status
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_file(request,id):
    instance = get_object_or_404(FileModel,id=id)
    serializer = FileSerializer(instance=instance,many=False)
    if instance is not None:
        file_path = instance.file.path 
        file_handle = open(file_path,'rb') # if we use this line then the file will be open and can't be deleted 
        return FileResponse(file_handle,as_attachment=True,filename=file_path)

@api_view(["GET"])
def get_all_file(request):
    instance = FileModel.objects.all()
    serializer = FileSerializer(instance=instance,many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def drop(request,id):
    instance = FileModel.objects.get(id=id)
    serializer = FileSerializer(instance=FileModel.objects.all(),many=True)
    if instance is not None:
        myfile = instance.file.path 
        if os.path.exists(myfile) and os.path.isfile(myfile):
            # print(f"can be dropped...{myfile}")
            # old_file = os.path.basename(myfile)
            # new_file = "sample.mp4"
            # old_dir = os.path.dirname(myfile)
            # latest_name = os.path.join(old_dir,new_file)
            # print(latest_name)
            # os.rename(myfile,latest_name)
            file_path = Path(myfile)
            if os.path.exists(file_path):
                        try:
                            file_path.unlink()  # This will delete the file
                            print("File deleted successfully")
                        except FileNotFoundError:
                            print("File not found")
                        except PermissionError:
                            print("Permission denied")
                        except Exception as e:
                            print(f"An error occurred: {e}")
            instance.delete()
            return Response(serializer.data)

@api_view(["PUT","GET"])
def rename_file(request,id):
     instance = get_object_or_404(FileModel,id=id)
     serializer = FileSerializer(instance=instance,data=request.data)
     if serializer.is_valid():
           # print(f"can be dropped...{myfile}")
            new_file = os.path.basename(request.data.get('file'))
            old_dir = os.path.dirname(instance.file.path)
            latest_name = os.path.join(old_dir,new_file)
            print(latest_name)
            # os.rename(myfile,latest_name)