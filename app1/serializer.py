from rest_framework.serializers import ModelSerializer 
from .models import Category, Table, Menu
from rest_framework import serializers

# serializer for Category
class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
        # fields=['name']
        # fields = ['id','name']
        # exclude=['name']


# same data post ra put garna namilney banauna

    # def save(self,**kwargs):
    #     validated_data=self.validated_data
    #     item = Category.objects.filter(name=self.validated_data.get('name')).count()
    #     if item>0:
    #         raise serializers.ValidateError({"message":"Data already exists"})
    #     return super().save(self.instance, **kwargs)
        
# same data put garna namilney banauna

    def create(self, validated_data):
        item = Category.objects.filter(name=self.validated_data.get('name')).count()
        if item>0:
            raise Exception({"message":"Data already exists"})
        return super().create(validated_data)
    

class MenuModelSerializer(ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model=Menu
        fields=['id','name','category_id','category','price','price_with_tax']
    
    def get_price_with_tax(self, menu:Menu):
        return menu.price * 0.13 + menu.price
    
        



    
# serializer for Table
class TableModelSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields='__all__'
        # fields=['name']
        # fields = ['id','name']
        # exclude=['name']


# class CategorySerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     name= serializer.CharField()
        
#     def create(self, validated_data):
#         return Category.objects.create(name= validated_data.get('name'))

#     # validated_data ma chai hamle api through haleko data aauxa
#     # {
#     # "name":"category1"
#     # }
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.save()
#         return instance
# yo chai model.py ma yesari hunxa 

# class Table(models.Model):
#     number=models.CharField(max_length=2)
#     is_available=models.BooleanField(default=True)

# hamle odels.py herera serializers ma yesari lekhxa

# class TableSerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     number=serializers.CharField()
#     is_available=serializers.BooleanField()

#     def create(self, validated_data):
#             return Table.objects.create(number= validated_data.get('number'))

#     def update(self, instance, validated_data):
#         instance.number=validated_data.get('number',instance.number)
#         instance.save()
#         return instance
    

