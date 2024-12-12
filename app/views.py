from django.shortcuts import render

# Create your views here.
def pictures(request):
    return render(request,'pictures.html')
