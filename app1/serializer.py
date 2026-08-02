from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)    # database bata read hunxa but yeslai post garda hudaina
    name=serializers.CharField()
    
    def create(self, validated_data):
        return Category.objects.create(name= validated_data.get('name'))

    # validated_data ma chai hamle api through haleko data aauxa
    # {
    # "name":"category1"
    # }
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance
# yo chai model.py ma yesari hunxa 

# class Table(models.Model):
#     number=models.CharField(max_length=2)
#     is_available=models.BooleanField(default=True)

# hamle odels.py herera serializers ma yesari lekhxa

class TableSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    number=serializers.CharField()
    is_available=serializers.BooleanField()


