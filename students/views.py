from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    
    students=['Aakriti',"Khushi","Susan"]
    return render(

        request, 'students/home.html',{"students": students}
                  )