from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import person

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj2=person.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})