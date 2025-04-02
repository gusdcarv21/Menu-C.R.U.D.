from django.shortcuts import render

from CRUD.models import produto

# Create your views here.

def menu(request):
  
    menu = []
    
    return render(request, 'menu.html')


def cadastrar(request):

        if request.method == 'POST':
            print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        descrição = request.POST.get('descrição')
        valor = request.POST.get('valor')
        quantidade_em_estoque = request.POST.get('quantidade_em_estoque')

        
        cadastrar=[]
        produto.nome = nome
        produto.descrição = descrição
        produto.preço

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