from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .serializer import CategorySerializer, TableSerializer
from .models import Category, Table

# Create your views here.
@api_view() #@api_view(['GET']) default ma get request hunxa
def category_list(request):
    catagories=Category.objects.all()
    serializer=CategorySerializer(catagories, many=True) # serialize, serialization: convert queryset to json
    return Response(serializer.data)

@api_view()
def table_list(request):
    tables=Table.objects.all()
    serializer=TableSerializer(tables, many=True)
    return Response(serializer.data)
