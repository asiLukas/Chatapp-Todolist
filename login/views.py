from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegisterForm()
            return redirect('/../../login/login')
    context = {
        'form': form}
    return render(request, 'registration/register.html', context)

