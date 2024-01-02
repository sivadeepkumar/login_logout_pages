from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
# import pdb


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def user_not_authenticated(user):
    print(user.is_authenticated)
    return not user.is_authenticated


@user_passes_test(user_not_authenticated, login_url='/accounts/login')
def login(request):
    if request.method == 'POST':
        # pdb.set_trace()
        return redirect('/')
    if user_not_authenticated() == True :
        return redirect('/')
    return render(request,'registration/login.html')



@login_required
def main(request):
    user = request.user
    print("Hi You Log-in Successfully")
    return render(request,'main.html')
    
    

@login_required
def logout(request):
    return render(request,'logout.html')


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CustomUser


@login_required
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = request.POST['role']  # Get role from the form
            user.save()
            return redirect('main')  # Redirect to the main page or login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

