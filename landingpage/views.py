from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Cliente

# Função para verificar se o usuário é admin
def is_admin(user):
    return user.is_superuser  # Verifica se o usuário é superusuário

# Página inicial com formulário
def index(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('sucesso')  # Redireciona para a página de sucesso
    else:
        form = ClienteForm()
    return render(request, 'landing_page/index.html', {'form': form})

# Página de sucesso
def sucesso(request):
    return render(request, 'landing_page/sucesso.html')

@login_required
@user_passes_test(is_admin, login_url='acesso_negado')  # Redireciona se não for admin
def respostas(request):
    clientes = Cliente.objects.all()
    return render(request, 'landing_page/respostas.html', {'clientes': clientes})


# Página de acesso negado
def acesso_negado(request):
    return render(request, 'landing_page/acesso_negado.html')