from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def ver_mais(request):
    return render(request, "ver_mais.html")