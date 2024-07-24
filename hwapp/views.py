from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hwappview(request):
    return HttpResponse('初めてのアプリが呼び出された！') #()を抜かしてはいけない！