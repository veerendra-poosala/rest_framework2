from django.shortcuts import render


def home(request):
    return render(request,'index.html',{'h_name':'rest_framework'})

