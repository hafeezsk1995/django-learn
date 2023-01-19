
from ast import Try
import json
import re
from rest_framework import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Customer, Deleviry, Interest, Person, Phone, Post,M1,M2
from django.db import connections; 
from django.db.models import F,Q
from configurations import settings



print("printed started")
posts = [
    {
        'author': 'hafeez',
        'title': 'Blog first 1',
        'content': 'First Post Content',
        'date_passed': 'August 27, 2018'
    },
    {
        'author': 'sams',
        'title': 'Blog first 2',
        'content': 'Second Post Content',
        'date_passed': 'August 28, 2018'
    }
]
# Create your views here.
def blog(request):
    return HttpResponse('<h1> Hello blog </h1>')

def home(request):
    # context = {
    #     'posts':posts
    # }
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About Page'})


from .models import MyModel
from .serializers import MyModelFrom, MyModelSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_protect 
from rest_framework.response import Response

# class FileUpload(viewsets.ModelViewSet):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer
#     authentication_classes = []
#     permission_classes=[]

#     def perform_create(self, serializer):
#         serializer.save()


class FileUpload(APIView):
    serializer_class = MyModelSerializer
    def post(self,request):
        print("file type",request.data['image_url'],type(request.data['image_url']))
        serializer = MyModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)




# class FileUpload()


# from sqlalchemy import 


class MyModelOperations(APIView):
    def get(self, request):
        print("helo")
        # for data in MyModel.objects.filter(title='nagara'):
        #     data.age +=1
        #     data.save()
        # return Response(True)
        MyModel.objects.filter(title='nagara').update(description='anu')
        return Response(True)


class DataMigration(APIView):
    def post(self,request):
        l1 = [1,2,3]
        l2 = [3,4,5]
        for d1 in l1:
            print("d1 times",d1)
            for d2 in l2:
                print("d2 times",d2)  
        
        # d1 = MyModel.objects.values_list('title',flat=True)
        # # for data in d1:
        # #     d2 = data['title']
        
        # d2 = M1.objects.values_list('name',flat=True)
        # # [    ]
        # if len(d1)!=0:
        #    my_objects = [M2.objects.create(title=d1_data) for d1_data in d1 
        #   ]
        # for d2_data in d2:
        #     print("da",d2_data)
        #     M2.objects.all().update(name=d2_data)

        # for d2_date in d2:
        #     my_objects.name = d2_date

        # # if len(d2)!=0:
        # #     my_data = []   
        # #    print("my_object",my_objects)
        # # M2(title=d1_data)
        # # for d2_data in d2]
        # M2.objects.bulk_create(my_objects)
        return Response(True)


class GetCreate(APIView):
    def post(self,request):
        d = MyModel.objects.filter(Q(title='basha')).get_or_create(title ='bhanu', defaults={'description': "good"})
        print(d,type(d))

        return Response(d[0])

from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def my_model_api(request):
    print("creating post")
    try:
        print("methods",request.method)
        if request.method == 'POST':
            print("creating post",json.loads(request.body))
            #MyModel.objects.create(**json.loads(request.body))
            
        if request.method == 'GET':
            print("hello")
            print('request id ',)    

        return HttpResponse("true")    
              
    except Exception as err:
        print("exception err",str(err))



class Getdata(APIView):
    def get(self):
        d = MyModel.objects.get(id=1)
        print("d",d)
        return HttpResponse("true")    

@csrf_protect   
def data(request):
    if request.method == 'POST':
        print("working")
        return JsonResponse({"Hu":True})

class One_One_Checking(APIView):
    def post(self,request):
        Phone.objects.create(number= "987654321",customer_id =2)
        return Response(True)

class Update_One_One_checking(APIView):
    def put(slef,request):
        Phone.objects.filter(id=1).update(customer_id=2)
        return Response(True)
class Get_One_One_Checking(APIView):
    def get(slef,request):
        d = Phone.objects.get(id=4).customer.no
        print("d",d)
        return Response(d)        

class Delete_customer(APIView):
    def put(slef,request):
        Customer.objects.filter(id=1).delete()
        return Response(True)


class DeleviryCreation(APIView):
    def post(slef,request):
        dele = Deleviry.objects.create(name= "dsdf")
        return Response(True) 


class ManyPost(APIView):
    def post(self, request):
        inter1 = Interest.objects.get(id=1)
        inter2 = Interest.objects.get(id=2)
        d  = Person.objects.create(name="hafeez")
        d.interest.add(inter1,inter2)

        return Response(True) 
# Getting interests from persons
class ManyGet(APIView):
    def get(self, request):
        c = Person.objects.get(id=4).interest.all()
        print("c",c)
        return Response(c)        

# Getting interests from persons
class ManyGetInterestsFromPersons(APIView):
    def get(self, request):
        c = Interest.objects.get(id=1).person.all()
        print("c",c)
        return Response(c)    

print("printed done")


class CheckFunInModels(APIView):
    def get(self,request):
        d = MyModel.objects.get(id=1)
        return Response (d.fun_check())


@csrf_exempt
def check_meta(request):
    if request.method == 'POST':
        print("startig the pointing")
        jsn = request.META
        print("jsn",jsn)
        #print("meta",request.META['CLIENT_ID'])
        client_id = request.META.get('HTTP_CLIENT_ID')
        client_secret = request.META.get('HTTP_CLIENT_SECRET')
        print("ids",client_id,client_secret)
        if (settings.client_id == client_id and settings.client_secret == client_secret):
            return HttpResponse (True)
        else:
            return HttpResponse (False)    

@csrf_exempt
def form_image_upload(request):
    if request.method == "POST":
        print("form variables checking",request.POST.get('age'))
        print("request.post",type(request.POST),request.POST)
        print("file",type(request.FILES),request.FILES)
        form = MyModelFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            "hjgj"
    return HttpResponse ("Uploaded files and darta")      



@csrf_exempt
def file_upload_fun_type(request):
    #serializer_class = MyModelSerializer
    if request.method == 'POST':
        print("post data",request.POST,request.FILES)
        # request.POST['image_url'] = request.FILES
        #print("file type",request.POST['image_url'],type(request.POST['image_url']))
        serializer = MyModelSerializer(data= request.POST)
        if serializer.is_valid():
            serializer.validated_data['image_url'] = request.FILES
           
            serializer.save()
        #obj = MyModel.objects.create(request.POST,request.FILES)
        return HttpResponse(True)



@csrf_exempt
def check_request(request):
    try:
        print("checking")
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            print("body",body)
        
    except Exception as e:
        print("except",e)   
    return HttpResponse(True)          




@csrf_exempt
def get_records(request):
    try:
        app = []
        if request.method == 'GET':
            print("callimng")
            if len(app) < 30:
                cred = LendersPaymentRecords.objects.filter(isAlreadyInvested = False).values('applicationId_id').distinct()
                for c in cred:
                    lpr_agg = LendersPaymentRecords.objects.filter(applicationId=c['applicationId_id']).aggregate(Sum('principalReceived'))['principalReceived__sum'] or 0
                    if lpr_agg < LenderPaymentSchedule.objects.filter(applicationId=c['applicationId_id'],isInActive = False,isAlreadyInvested = False).aggregate(Sum('lenderPrincipalReceived'))['lenderPrincipalReceived__sum'] or 0 :
                        pass
                    else:
                        app.append(c['applicationId_id'])      
            return JsonResponse(app,safe=False)
    except Exception as ex:
        return JsonResponse(app,safe=False)

@csrf_exempt
def check_borrower_emi(request):
    
    if request.method == 'GET':
        b = BorrowerAccrualEMISchedule.objects.filter(applicationId_id__in=app,isInvoiceCleared = False,isInActive = False).values('applicationId_id','id').distinct()
        return JsonResponse(list(b),safe=False)



#  dy_total_interest = dy_total_records.aggregate(Sum('interest'))['interest__sum'] if dy_total_records.aggregate(Sum('interest'))['interest__sum'] != None else 0



#  st_total_principal = LenderPaymentSchedule.objects.filter(applicationId = application,lenderId = lender,
#                                                           replacementApplicationId = replacementApplicationId,
#                                                           isInActive = False).aggregate(Sum('lenderPrincipalReceived'))['lenderPrincipalReceived__sum'] or 0

#         st_total_interest = LenderPaymentSchedule.objects.filter(applicationId = application,lenderId = lender,
#                                                           replacementApplicationId = replacementApplicationId,
#                                                           isInActive = False).aggregate(Sum('lenderMonthlnterestReceived'))['lenderMonthlnterestReceived__sum'] or 0


class ListWithDifferent(APIView):
    def get(self,*args, **kwargs):
        # try:
        #     p = Person.objects.all().values()[0:5]
        #     return Response(p)
        # except Exception as e:
        #     print("e")    

        # try:
        #     p = Person.objects.all().order_by('-id').values()[0:5]
        #     return Response(p)
        # except Exception as e:
        #     print("e")    

        # try:
        #     p = Person.objects.all().values()[5:]
        #     return Response(p)
        # except Exception as e:
        #     print("e")     

        try:
            p = Person.objects.all().order_by('-id').values()[1:]
            return Response(p)
        except Exception as e:
            print("e") 