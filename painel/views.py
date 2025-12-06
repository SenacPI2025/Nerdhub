from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
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
            return redirect('painel:dashboard')
        else:
            return render(request, 'painel/login.html', {'erro': True})

    return render(request, 'painel/login.html')


@login_required
@user_passes_test(is_admin)
def dashboard(request):
    return render(request, 'painel/dashboard.html')


@login_required
@user_passes_test(is_admin)
def produtos_list(request):
    produtos = Product.objects.all()
    return render(request, 'painel/produtos_list.html', {'produtos': produtos})


@login_required
@user_passes_test(is_admin)
def produto_novo(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('painel:produtos_list')
    else:
        form = ProductForm()
    
    return render(request, 'painel/produtos_form.html', {
        'form': form,
        'modo': 'novo'
    })


@login_required
@user_passes_test(is_admin)
def produto_editar(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('painel:produtos_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'painel/produtos_form.html', {
        'form': form,
        'modo': 'editar',
        'product': product,
        'id': id
    })


@login_required
@user_passes_test(is_admin)
def usuarios_list(request):
    return render(request, 'painel/usuarios_list.html')


@login_required
@user_passes_test(is_admin)
def pedidos_list(request):
    return render(request, 'painel/pedidos_list.html')