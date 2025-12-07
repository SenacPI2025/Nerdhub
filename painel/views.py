from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm, ProductImageForm

def is_admin(user):
    return user.is_superuser or user.is_staff

def login_painel(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            # Check if user is admin/staff - if so, go to panel, otherwise go to profile
            if user.is_superuser or user.is_staff:
                return redirect('painel:dashboard')
            else:
                # For regular users, redirect to profile or home page
                return redirect('nucleo:index')  # Change this to user profile URL when ready
        else:
            return render(request, 'painel/login.html', {'erro': True})

    return render(request, 'painel/login.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticar e logar o usuário após o registro
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('nucleo:index')
    else:
        form = UserCreationForm()
    return render(request, 'painel/registro.html', {'form': form})

def logout_painel(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('nucleo:index')

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    return render(request, 'painel/dashboard.html')

@login_required
@user_passes_test(is_admin)
def produtos_list(request):
    produtos = Product.objects.all().order_by('-created_at')
    return render(request, 'painel/produtos_list.html', {'produtos': produtos})

@login_required
@user_passes_test(is_admin)
def produto_novo(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save()
            # Salvar imagens adicionais
            images = request.FILES.getlist('images')
            if images:
                for image in images:
                    ProductImage.objects.create(product=produto, image=image)
            return redirect('painel:produtos_list')
    else:
        form = ProductForm()
    return render(request, 'painel/produto_form.html', {'form': form, 'titulo': 'Novo Produto'})

@login_required
@user_passes_test(is_admin)
def produto_editar(request, id):
    produto = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            produto = form.save()
            # Salvar imagens adicionais
            images = request.FILES.getlist('images')
            if images:
                for image in images:
                    ProductImage.objects.create(product=produto, image=image)
            return redirect('painel:produtos_list')
    else:
        form = ProductForm(instance=produto)
    return render(request, 'painel/produto_form.html', {'form': form, 'titulo': 'Editar Produto', 'produto': produto})

@login_required
@user_passes_test(is_admin)
def usuarios_list(request):
    usuarios = User.objects.all().order_by('-date_joined')
    return render(request, 'painel/usuarios_list.html', {'usuarios': usuarios})

@login_required
@user_passes_test(is_admin)
def pedidos_list(request):
    return render(request, 'painel/pedidos_list.html')