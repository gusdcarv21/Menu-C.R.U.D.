from django.shortcuts import render

from CRUD.models import produto

# Create your views here.

def menu(request):
  
    menu = []
    
    return render(request, 'menu.html')


def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descrição = request.POST.get('descrição')
        valor = request.POST.get('valor')
        quantidade_em_estoque = request.POST.get('quantidade_em_estoque')

        novo_produto = produto(
            nome=nome,
            descrição=descrição,
            preço=valor,
            quantidade_em_estoque=quantidade_em_estoque
        )

        novo_produto.save()  # <-- isso salva no banco

    return render(request, 'cadastrar.html')

def listar(request):
    produtos = produto.objects.all()
    
    return render (request, 'listar.html', {'produtos':produtos})

def atualizar(request):
    atualizar=[]
    return render (request, 'atualizar.html')

def deletar(request):
    deletar=[]
    return render (request, 'deletar.html')