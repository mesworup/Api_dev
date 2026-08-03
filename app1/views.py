from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .serializer import *
from .models import *
# Create your views here.

# CLASS BASED VIEW
# VIEWSET:

from rest_framework.viewsets import ViewSet, ModelViewSet
class CategoryModelViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategoryModelSerializer

    def destroy(self,request,id):
        category=Category.objects.get(id=id)
        item=OrderMenu.objects.filter(menu__category=category).count()
        if item>0:
            return Response({"message":"Data cant be deleted. Protected foreign Key in ordermenu"})
        category.delete()
        return Response({"message":"Data has been deleted."})


# class CategoryViewSet(ViewSet):
#     def list(self,request):
#         catagory=Category.objects.all()
#         serializer=CategorySerializer(catagory, many=True) 
#         return Response(serializer.data)

#     def create(self,request):
#         serializer=CategorySerializer(data=request.data)    # deserialize, deserializer: convert json into quertyset
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# class CategoryDetailView(ViewSet):
#     def retrieve(self,request,id):
#         category=Category.objects.get(id=id)
#         serializer=CategorySerializer(category)
#         return Response(serializer.data)

#     def update(self,request,id):
#         category=Category.objects.get(id=id)
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def destroy(self,request,id):
#         category=Category.objects.get(id=id)
#         item=OrderMenu.objects.filter(menu__category=category).count()
#         if item>0:
#             return Response({"message":"Data cant be deleted. Protected foreign Key in ordermenu"})
#         category.delete()
#         return Response({"message":"Data has been deleted."})





from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class CategoryGeneric(ListCreateAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer
    
# class CategoryDetailGeneric(RetrieveUpdateDestroyAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer

# # hamro delete ma validations haru xa thats why yesari lekhney ani override gardinxa
#     def delete(self,request,pk):
#         #return self.destroy(request, pk)
#         category=self.get_object()
#         item=OrderMenu.objects.filter(menu__category=category).count()
#         if item>0:
#             return Response({"message":"Data cant be deleted. Protected foreign Key in ordermenu"})
#         category.delete()
#         return Response({"message":"Data has been deleted."})



# class TableGeneric(ListCreateAPIView):
#     queryset=Table.objects.all()
#     serializer_class=TableSerializer
    
# class TableDetailGeneric(RetrieveUpdateDestroyAPIView):
#     queryset=Table.objects.all()
#     serializer_class=TableSerializer




# GENERIC APIVIEW with mixin
# from rest_framework.generics import GenericAPIView
# from rest_framework import mixins

# class CategoryGeneric(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer
    
#     def get(self,request):
#         return self.list(self,request)
#         # catagory=self.get_queryset()
#         # serializer=self.serializer_class(catagory, many=True) 
#         # return Response(serializer.data)

#     def post(self,request):
#         return self.create(self,request)
#     #     serializer=self.serializer_class(data=request.data)    # deserialize, deserializer: convert json into quertyset
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     #return Response({"message":"Data Added,","result":serializer.data})
#     #     return Response(serializer.data)
    

# class CategoryDetailGeneric(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer
    
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#         # catagory=self.get_object()
#         # serializer=self.serializer_class(catagory) 
#         # return Response(serializer.data)

#     def put(self,request,pk):
#         return self.update(request, pk)
#         # category=self.get_object()
#         # serializer=CategorySerializer(category,data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data)
    
#     def delete(self,request,pk):
#         #return self.destroy(request, pk)
#         category=self.get_object()
#         item=OrderMenu.objects.filter(menu__category=category).count()
#         if item>0:
#             return Response({"message":"Data cant be deleted. Protected foreign Key in ordermenu"})
#         category.delete()
#         return Response({"message":"Data has been deleted."})
        
        
    

# class TableGeneric(GenericAPIView):
#     queryset=Table.objects.all()
#     serializer_class=TableSerializer
#     def get(self,request):
#         table=self.get_queryset()
#         serializer=self.serializer_class(table, many=True) 
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=self.serializer_class(data=request.data)    # deserialize, deserializer: convert json into quertyset
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         #return Response({"message":"Data Added,","result":serializer.data})
#         return Response(serializer.data)    



# # API VIEW
# from rest_framework.views import APIView

# # fetch all data
# class CategoryView(APIView):
#     def get(self,request):
#         catagories=Category.objects.all()
#         serializer=CategorySerializer(catagories, many=True) 
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=CategorySerializer(data=request.data)    # deserialize, deserializer: convert json into quertyset
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         #return Response({"message":"Data Added,","result":serializer.data})
#         return Response(serializer.data)


# # fetch single data
# class CategoryViewSingle(APIView):
#     def get(self,request,id):
#         category=Category.objects.get(id=id)
#         serializer=CategorySerializer(category)
#         return Response(serializer.data)

#     def put(self,request,id):
#         category=Category.objects.get(id=id)
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self,request,id):
#         category=Category.objects.get(id=id)
#         item=OrderMenu.objects.filter(menu__category=category).count()
#         if item>0:
#             return Response({"message":"Data cant be deleted. Protected foreign Key in ordermenu"})
#         category.delete()
#         return Response({"message":"Data has been deleted."})





# FUNCTION BASED VIEW
# all data
# @api_view(['GET','POST']) #@api_view(['GET']) default ma get request hunxa
# def category_list(request):
#     if request.method=='GET':
#         catagories=Category.objects.all()
#         serializer=CategorySerializer(catagories, many=True) # serialize, serialization: convert queryset to json
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=CategorySerializer(data=request.data)    # deserialize, deserializer: convert json into quertyset
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # return Response({"message":"Data Added,","result":serializer.data})
#         return Response(serializer.data)
 
# # single data fetch ,delete and put 
# @api_view(['GET','DELETE','PUT'])
# def category_detail(request,id):
#     category=Category.objects.get(id=id)
#     if request.method=='GET':
#         serializer=CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method=='DELETE':
#         item=OrderMenu.objects.filter(menu__category=category).count()
#         if item>0:
#             return Response({"message":"Data cant be deleted. Protected foreign Key in ordermenu"})
#         category.delete()
#         return Response({"message":"Data has been deleted."})
#     elif request.method=='PUT':
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view()
# def table_list(request):
#     tables=Table.objects.all()
#     serializer=TableSerializer(tables, many=True)
#     return Response(serializer.data)
