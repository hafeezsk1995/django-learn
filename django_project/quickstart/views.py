from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Jinnja template

def post_detail(request,number):
    return render(request,'post_detail.html',{'number':number})


# Create your views here.


# function based 
@api_view(['post','GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializers(student_obj,many=True)
    return Response({"status":200,"result":serializer.data})

# function based 
@api_view(['post'])
def post_student(request):
    serializer = StudentSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"status":200,"result":serializer.data})
    

@api_view(['post'])
def update_student(request,id):
    stud = Student.objects.get(id=id)
    serializer = StudentSerializers(instance=stud,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"status":200,"result":serializer.data})    

@api_view(['delete'])
def delete_student(request,id):
    stud = Student.objects.get(id=id)
    stud.delete()
    return Response("student is deleted")   


#Generics apiview mixins
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def get(self,request):
        return self.list(request)

class StudentCreate(GenericAPIView,CreateModelMixin):
    def get(self,request):
        return self.create(request)

        