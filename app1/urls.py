from django.urls import path
from .views import *
from rest_framework import routers

route = routers.SimpleRouter()
route.register('category',CategoryModelViewSet)


urlpatterns = [
    # path('category/', category_list),
    # path('table/', table_list),
    # path('category/<id>/', category_detail)
    # path('category/', CategoryModelViewSet.as_view({'get':'list','post':'create'})),
    # path('category/', CategoryGeneric.as_view()),
    # path('category/<pk>/', CategoryDetailGeneric.as_view()),
    # # path('category/<id>/', CategoryViewSingle.as_view()),
    # path('table/', TableGeneric.as_view()),
    # path('table/<pk>/', TableDetailGeneric.as_view()),    

] + route.urls
