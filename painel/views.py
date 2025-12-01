from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_painel(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('painel:dashboard')
        else:
            return render(request, 'painel/login.html', {'erro': True})

    return render(request, 'painel/login.html')


@login_required
def dashboard(request):
    return render(request, 'painel/dashboard.html')


@login_required
def produtos_list(request):
    return render(request, 'painel/produtos_list.html')


@login_required
def produto_novo(request):
    return render(request, 'painel/produtos_form.html', {'modo': 'novo'})


@login_required
def produto_editar(request, id):
    return render(request, 'painel/produtos_form.html', {'modo': 'editar', 'id': id})


@login_required
def usuarios_list(request):
    return render(request, 'painel/usuarios_list.html')


@login_required
def pedidos_list(request):
    return render(request, 'painel/pedidos_list.html')
