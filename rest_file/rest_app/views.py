from django.shortcuts import get_object_or_404, render
from .models import fileModel
from .serializers import fileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# file uploading view
@api_view(['POST'])
def fileupload(request):
    if request.method == "POST":  
        serializer = fileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# get all files      
@api_view(['GET'])
def getfile(request):
    instance = fileModel.objects.all()
    serializer = fileSerializer(instance=instance,many=True)
    return Response(serializer.data)

# delete a file 
@api_view(['DELETE'])
def deletefile(request,id):
    instance = get_object_or_404(fileModel,id=id)
    serializer = fileSerializer(instance=fileModel.objects.all(),many=True)
    if instance is not None:
        instance.delete()
        return Response(serializer.data)

# update a file record
@api_view(['PUT'])
def updatefile(request,id):
    instance = get_object_or_404(fileModel,id=id)
    serializer = fileSerializer(instance=instance,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    serializer = fileSerializer(instance=instance,many=False)
    return Response(serializer.data)