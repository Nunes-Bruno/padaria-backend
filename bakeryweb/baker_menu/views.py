from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'painel_inicial/home.html')

def cadastro(request):
    return render(request, 'painel_inicial/cadastro.html')