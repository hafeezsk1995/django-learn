from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def blog_view(request):
    return Response({"Hello Testing"})


