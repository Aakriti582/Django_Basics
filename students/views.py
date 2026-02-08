from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    is_class_active=True    
    return render(

        request, 'students/home.html',
        {"is_class_active":is_class_active}
                  ) 