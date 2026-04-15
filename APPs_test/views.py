from django.shortcuts import*
from django.http import*

#Create your views here.
def http_test(request):
    return HttpResponse("<h1> This note has been written in HTML format!</h1>")

def json_test(request):
    return JsonResponse({"first prt":"This note has been ", "last prt":"written in JSON format!"})