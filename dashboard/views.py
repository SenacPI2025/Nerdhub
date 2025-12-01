from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_staff(user):
    return user.is_staff  # Só admin/staff pode ver

@login_required
@user_passes_test(is_staff)
def index(request):
    return render(request, 'dashboard/index.html', {'page_name': 'dashboard'})
