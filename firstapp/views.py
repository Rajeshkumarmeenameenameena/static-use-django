from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    my_dict={
        'company':'maruti',
             'onername':'rajesh' ,
             'car':['maruti','suziki','honda','tata']}

    return render(request,'app/home.html',my_dict)

def base(request):
    return render(request,'app/base.html')