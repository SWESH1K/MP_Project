from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def generate(request):
    return render(request, 'generate.html')