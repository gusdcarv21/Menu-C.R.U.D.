from django.shortcuts import render

# Create your views here.

def menu(request):
  
    menu = []
    
    return render(request, 'menu.html')


def cadastrar(request):

    cadastrar=[]

    return render(request, 'cadastrar.html')

def listar(request):
    listar=[]
    return render (request, 'listar.html')

def atualizar(request):
    atualizar=[]
    return render (request, 'atualizar.html')

def deletar(request):
    deletar=[]
    return render (request, 'deletar.html')