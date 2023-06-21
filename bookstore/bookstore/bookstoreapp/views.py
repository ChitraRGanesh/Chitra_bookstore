from django.http import HttpResponse
from django.shortcuts import render
from . models import book
# Create your views here.

def index(request):
    obj=book.objects.all()
    return render(request,'index.html',{'result':obj})
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
# def reg_form(request):
#     return render(request,'reg_form.html')
def reg_form(request):
    # if request.method == 'POST':
    registration_successful = False
    if request.method == 'POST':
        registration_successful=True
    return render(request, 'reg_form.html', {'reg_form_successful': registration_successful})
    # else:
    #     return render(request, 'reg_form.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')