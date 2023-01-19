from django.shortcuts import render
from .models import Blue
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class CreateBlue(APIView):
    def post(self, request, *args, **kwargs):
        b = Blue.objects.create(title = request.data['title'],description = request.data['description'],age = request.data['age'])
        # b.save()
        return Response(True)


class GetBlue(APIView):
    def get(self, *args, **kwargs):
        b = Blue.objects.all().values()
        return Response(b)