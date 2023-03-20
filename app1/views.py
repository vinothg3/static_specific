from django.shortcuts import render

# Create your views here.
def static_specific(request):
    return render(request,"static_specific.html")