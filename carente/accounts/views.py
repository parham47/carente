from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required
def profile(request):
    return render(request , 'accounts/profile.html')


@user_passes_test(lambda u: not u.is_authenticated , '/' , None)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request , 'registration/register.html' , { 'form' : form })