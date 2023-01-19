from rest_framework import serializers
from .models import MyModel
from django import forms
class MyModelSerializer(serializers.ModelSerializer):
    print("img_url")
    # image_url = serializers.ImageField(required=False)
    #print("img_url",type(image_url))

    class Meta:
        model = MyModel
        fields = ['id','title', 'description', 'image_url']



class MyModelFrom(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'

