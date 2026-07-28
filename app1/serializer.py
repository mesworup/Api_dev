from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id= serializers.IntegerField()
    name=serializers.CharField()
    
    
# yo chai model.py ma yesari hunxa 

# class Table(models.Model):
#     number=models.CharField(max_length=2)
#     is_available=models.BooleanField(default=True)

# hamle odels.py herera serializers ma yesari lekhxa

class TableSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    number=serializers.CharField()
    is_available=serializers.BooleanField()


