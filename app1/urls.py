from django.urls import path
from .views import *
urlpatterns = [
    # path('category/', category_list),
    # path('table/', table_list),
    # path('category/<id>/', category_detail)
    
    path('category/', CategoryGeneric.as_view()),
    path('category/<pk>/', CategoryDetailGeneric.as_view()),
    # path('category/<id>/', CategoryViewSingle.as_view()),
    path('table/', TableGeneric.as_view()),
    
    
    
    
]
