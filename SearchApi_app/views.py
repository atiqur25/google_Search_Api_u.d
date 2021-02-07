from django.shortcuts import render


# Create your views here.

def HomepageView(request):
    return render(request, 'google.html')
